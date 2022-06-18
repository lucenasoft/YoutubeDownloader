from pytube import YouTube

link = input('URL YouTube: ')

yt = YouTube(f'{link}')
print(f'Baixar: {yt.title} ?')
question_ = ''
while question_ != 'N' and question_ != 'S':
    question_ = str(input('Continuar? [S/N] ')).upper()
if question_ == 'S':
    yt.streams.get_by_resolution('720p').download()
    print('Finalizado!')
if question_ == 'N':
    print('Tente novamente!')