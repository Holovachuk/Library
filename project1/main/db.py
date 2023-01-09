
users = [
    {
        'login': 'lera',
        'password': 'val228',
        'img': 'https://www.meme-arsenal.com/memes/0a2f97e29a2a95c781d322ff3dc50d6b.jpg',
        'isAdmin': False
    },
    {
        'login': 'zheka',
        'password': 'zkh',
        'img': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRrxguXcGMjtKPsxXlShapGw7X3f-mgSUH-xodjs7krz60rWOwV3brX3po60gUnnI09hL0&usqp=CAU',
        'isAdmin': False
    },
    {
        'login': 'admin',
        'password': 'aaaddd',
        'img': 'https://koshka.top/uploads/posts/2021-12/1639030708_1-koshka-top-p-koshki-rzhut-1.jpg',
        'isAdmin': True
    }
]

books = [
    {
        'name': 'Шерлок Холмс',
        'author': 'Артур Конан-Дойль',
        'genre': 'Детектив',
        'img': 'https://static.yakaboo.ua/media/catalog/product/2/0/20_2_39.jpg',
     
        'about': 'Золотая классика!',
        'comments': [
            {
                'user': users[0],
                'comment': "Очень интересно!",
                'raiting': 8
            },
        ]
    },
    {
        'name': 'Убийство в "Восточном экспрессе"',
        'genre': 'Детектив',
        'author': 'Агата Кристи',
        'img': 'https://cdn.eksmo.ru/v2/ITD000000000911032/COVER/cover1__w220.jpg',
        'about': 'Для особых ценителей жанра',
        'comments': [
            {
                'user': users[1],
                'comment': "Не оторваться!",
                'raiting': 9
            }
        ]
    },
    {
        'name': 'Портрет Дориана Грея',
        'genre': 'Роман',
        'author': 'Оскар Уайлд',
        'img': 'https://s1.livelib.ru/boocover/1002060701/200x305/fa2f/Portret_Doriana_Greya.jpg',
        'about': 'Про человеческую натуру',
        'comments': [
            {
                'user': users[2],
                'comment': "А портрет хорош.",
                'raiting': 10
            }
        ]
    },
    {
        'name': 'Оно',
        'genre': 'Ужасы',
        'author': 'Стивен Кинг',
        'img': 'https://knijky.ru/sites/default/files/styles/264x390/public/100166.jpg?itok=4rlY7J99',
        'about': 'Для любетелй пощекотать нервы',
        'comments': [
            {
                'user': users[0],
                'comment': "Страшно, страшно, очень страшно..",
                'raiting': 6
            }
        ]
    },
]

genre = 'All'
genres = ['All']

for book in books:
    if not genres.__contains__(book['genre']):
        genres.append(book['genre'])
    
    if book['comments'] and len(book['comments']) > 0:
        middle = 0
        for comment in book['comments']:
            middle += int(comment['raiting'])
    
    book['raiting'] = int(middle/len(book['comments']))

isLogin = False
isAdmin = False

user = None

def GetBookByName(name: str):
    for book in books:
        if(book['name'] == name):
            return book
    return None

def CheckRaiting():
    for rest in books:
        if rest['comments'] and len(rest['comments']) > 0:
            middle = 0
            for comment in rest['comments']:
                middle += int(comment['raiting'])
    
        rest['raiting'] = int(middle/len(rest['comments']))

def CheckGeners():
    genres.clear()
    genres.append('All')
    for book in books:
        if not genres.__contains__(book['genre']):
            genres.append(book['genre'])

