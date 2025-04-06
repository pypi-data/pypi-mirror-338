from youtube_transcript_api import YouTubeTranscriptApi
import re
from typing import Dict, Any, List, Optional


class YouTubeTranscriptExtractor:
    """
    Класс для извлечения и обработки транскрипций YouTube видео
    """
    
    def __init__(self):
        """
        Инициализация экстрактора транскрипций
        """
        # YouTube паттерны для извлечения ID из URL
        self.youtube_patterns = [
            r'(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})',
            r'youtube\.com/embed/([a-zA-Z0-9_-]{11})',
            r'youtube\.com/v/([a-zA-Z0-9_-]{11})'
        ]
    
    def extract_video_id(self, url: str) -> Optional[str]:
        """
        Извлечение ID видео из URL YouTube
        
        Args:
            url: URL YouTube видео
            
        Returns:
            ID видео или None, если ID не найден
        """
        for pattern in self.youtube_patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        
        return None
    
    def clean_transcript(self, transcript_text: str) -> str:
        """
        Функция для простой очистки и форматирования транскрипции
        
        Args:
            transcript_text: Текст транскрипции
            
        Returns:
            Отформатированный текст
        """
        if transcript_text.startswith("Ошибка"):
            return transcript_text
            
        # Удаляем повторяющиеся пробелы
        clean_text = ' '.join(transcript_text.split())
        
        # Разбиваем длинный текст на абзацы по 500 символов
        paragraphs = [clean_text[i:i+500] for i in range(0, len(clean_text), 500)]
        
        # Соединяем абзацы с двойным переносом строки
        formatted_text = '\n\n'.join(paragraphs)
        
        return formatted_text
    
    def list_languages(self, url: str) -> List[str]:
        """
        Список языков для данного видео
        """
        video_id = self.extract_video_id(url)
        return [transcript.language_code for transcript in YouTubeTranscriptApi().list(video_id=video_id)]
    
    def process_transcript(self, url: str, languages: str = "ru,en") -> Dict[str, Any]:
        """
        Основной метод для получения и обработки транскрипции
        
        Args:
            url: URL YouTube видео
            languages: Языки для поиска транскрипции (через запятую)
            
        Returns:
            Словарь с результатом обработки
        """
        # Проверяем, является ли URL ссылкой на YouTube
        if "youtube.com" not in url and "youtu.be" not in url:
            return {
                "success": False,
                "error": "Предоставленный URL не является ссылкой на YouTube видео"
            }
        
        # Получаем ID видео
        video_id = self.extract_video_id(url)
        if not video_id:
            return {
                "success": False,
                "error": "Не удалось извлечь ID видео из предоставленной ссылки"
            }
        
        # Получаем список языков
        lang_list = languages.split(",")
        
        try:
            # Получаем транскрипцию
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=lang_list)
            
            # Проверяем, что мы получили данные
            if not transcript_list:
                return {
                    "success": False,
                    "error": "Транскрипция не найдена для этого видео"
                }
                
            # Ручное форматирование текста из списка словарей
            formatted_transcript = ""
            for entry in transcript_list:
                if 'text' in entry:
                    formatted_transcript += entry['text'] + " "
            
            # Очищаем и форматируем текст
            formatted_text = self.clean_transcript(formatted_transcript.strip())
            
            return {
                "success": True,
                "transcript": formatted_text,
                "url": url,
                "video_id": video_id
            }
        except Exception as e:
            error_message = str(e)
            if "No transcript found" in error_message:
                error = f"Транскрипция не найдена для этого видео на языках {languages}"
            elif "Subtitles are disabled" in error_message:
                error = "Субтитры отключены для этого видео"
            else:
                error = f"Ошибка при получении транскрипции: {error_message}"
                
            return {
                "success": False,
                "error": error,
                "url": url,
                "video_id": video_id
            }


# Создаем экземпляр класса для использования в MCP
_extractor = YouTubeTranscriptExtractor()


def get_transcript(url: str, languages: str = "ru,en") -> Dict[str, Any]:
    """
    MCP обработчик для получения транскрипции YouTube видео
    
    Args:
        url: URL YouTube видео
        languages: Языки для поиска транскрипции (через запятую)
        
    Returns:
        Словарь с результатом обработки
    """
    return _extractor.process_transcript(url, languages) 