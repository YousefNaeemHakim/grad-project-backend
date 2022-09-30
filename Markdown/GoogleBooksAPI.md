## Google Books API Quick Links

- [API Overview](https://developers.google.com/books/docs/overview)
- [Getting Started](https://developers.google.com/books/docs/v1/getting_started)<br>
- [Using the API](https://developers.google.com/books/docs/v1/using)<br>

## API Endpoint
`https://www.googleapis.com/books/v1/volumes?q=${Book}` <br>  *The (book) argument is the passed variable from the User* <br>
*الكتاب اللي اليورز بيبحث عنه*

## Live Project that will help a lot 
- [Project Link](https://liyasthomas.github.io/books/)
- [Project Repo](https://github.com/liyasthomas/books) 

## Ex. for a returned JSON Object ( All Book Attributes)
```JSON
{
    "title": "١٢ قاعدة للحياة",
    "subtitle": "ترياق للفوضى",
    "authors": ["جوردان بيترسون"],
    "publisher": "Dar Attanweer",
    "description": "ساعد جوردان بيترسون الملايين حول العالم من أجل أن يحظوا بحياة منتجة قيّمة. والآن حان دورك. “المثقف الأكثر تأثيرًا الآن في العالم الغربي” The New York Times ليس من الضروري أن تتفق مع آراء بيترسون السياسية حتى تُعجب بهذا الكتاب، فلو تغاضيت عن تصنيفه ككتاب مساعدة ذاتية سترى أنه كتاب مذهل.. جوردان بيترسون عبقري في تناوله لمواضيع كتابه.. كتاب شامل ومشاكس وواقعي في آن. يحاول بيترسون في كتابه هذا إعادتنا إلى ما يعتقد أنه الحقيقة والجمال والخير..تستطيع اعتبار كتاب 12 قاعدة للحياة أرقى ما يمكن أن يكونه كتاب للمساعدة الذاتية.. وأيًا كان تصنيفك له فإن قراءته مزلزلة.بيترسون أصيل في تميّزه ولا يشبه أحدًا من المفكرين المعاصرين.بيترسون شخصية كاريزماتية شديدة الفصاحة، يقدم نموذجًا جديًا لنمط الشخصية العامة، فاليوتيوب ووسائل التواصل الاجتماعي تجعله يصل إلى أكبر شريحة ممكنة من الناس ليتقدم بذلك على سابقيه أمثال برتراند رسل وإيزايا برلين","industryIdentifiers": [{"type": "ISBN_13",
    "identifier": "9786144721216"},
    { 
        "type": "ISBN_10",
        "identifier": "6144721215"}],
        "readingModes": 
        {
            "text": false,"image": true    
        },
            "pageCount": 560,
            "printType": "BOOK",
            "categories": ["Psychology"],
            "maturityRating": "NOT_MATURE",
            "allowAnonLogging": true,
            "contentVersion": "0.0.1.0.preview.1","panelizationSummary": 
            {
                "containsEpubBubbles": false,"containsImageBubbles": false
            },
            "imageLinks": 
            { 
                "smallThumbnail": "http://books.google.com/books/content?id=2rf8DwAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
                "thumbnail": "http://books.google.com/books/content?id=2rf8DwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"},"language": "ar",
                "previewLink": "http://books.google.com.eg/books?id=2rf8DwAAQBAJ&pg=PA1&dq=rules-for-life&hl=&cd=1&source=gbs_api",
                "infoLink": "https://play.google.com/store/books/details?id=2rf8DwAAQBAJ&source=gbs_api","canonicalVolumeLink": "https://play.google.com/store/books/details?id=2rf8DwAAQBAJ"
            }

```

## All the Important Attributes
- title
- authors
- description
- categories
- imageLinks
  - imageLinks.smallThumbnail
  - imageLinks.thumbnail
- language
- previewLink
- infoLink
- saleInfo
  - saleInfo.listPrice
  - saleInfo.buyLink