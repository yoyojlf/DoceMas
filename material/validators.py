import os 
from django.core.exceptions import ValidationError

def valid_extension(value):
    ext = os.path.splitext(value.name)[1]

    valid_text = [ '.txt', '.doc', '.docx']
    valid_image = [ '.jpg', '.gif', '.bmp', '.png']
    valid_video = ['.avi', '.mp4', '.mpeg', '.mwv']
    valid_execute = ['.exe', '.bat', '.dll', '.sys']
    valid_audio = ['.mp3', '.wav', '.wma']
    valid_compress = ['.zip', '.rar', '.tar']
    valid_read = ['.pdf', '.epub', '.azw', '.ibook']
    
    if not ext.lower() in valid_text: 
        raise ValidationError("Archivos de texto permitidos: .txt, .doc, .docx")

    if(not ext.lower() in valid_image): 
        raise ValidationError("Archivos de imagen permitidos: .jpg, .gif, .bmp, .png")

    if(not ext.lower() in valid_video): 
        raise ValidationError("Archivos de video permitidos: .avi, .mp4, .mpeg, .mwv")

    if(not ext.lower() in valid_execute): 
        raise ValidationError("Archivos ejecutables permitidos: .exe, .bat, .dll, .sys")

    if(not ext.lower() in valid_audio): 
        raise ValidationError("Archivos de audio permitidos: .mp3, .wav, .wma")

    if(not ext.lower() in valid_compress): 
        raise ValidationError("Archivos compresos permitidos: .zip, .rar, .tar")

    if(not ext.lower() in valid_read): 
        raise ValidationError("Archivos de texto permitidos: .pdf, .epub, .azw, .ibook")