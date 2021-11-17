
import re

def processing(text, *args, **kwargs):
    while True:
        text = re.sub(r' mil inscritos', '00', text)
        text = re.sub(r' mi de inscritos', '00000', text)
        text = re.sub(r' mil inscritos', '000', text)
        text = re.sub(r' mil inscritos', '00', text)
        text = re.sub(r' mi de inscritos', '0000', text)
        text = re.sub(r' inscritos', '', text)
        text = re.sub(r' inscrito', '', text)
        text = re.sub(r'Um', '1', text)
        text = re.sub(r' mil visualizações', '00', text)
        text = re.sub(r' mi de visualizações', '00000', text)
        text = re.sub(r' mil visualizações', '000', text)
        text = re.sub(r' mil visualizações', '00', text)
        text = re.sub(r' mi de visualizações', '0000', text)
        text = re.sub(r' visualizações', '', text)
        text = re.sub(r' visualização', '', text)
        text = re.sub(r'Uma', '1', text)
        text = re.sub(r' mil vídeos', '00', text)
        text = re.sub(r' mi de vídeos', '00000', text)
        text = re.sub(r' mil vídeos', '000', text)
        text = re.sub(r' mil vídeos', '00', text)
        text = re.sub(r' mi de vídeos', '0000', text)
        text = re.sub(r' vídeos', '', text)
        text = re.sub(r' vídeos', '', text)
        text = re.sub(r' vídeo', '', text)
        text = re.sub(r'Um', '1', text)
        text = re.sub(r' mil', '00', text)
        text = re.sub(r' mi de', '00000', text)
        text = re.sub('[^A-Za-z0-9]+', ' ', text)
        return text
