page = '''<!DOCTYPE html><html><head>
    <meta charset="utf-8">
    <title>Fuck U</title>
</head>
<body>
    <!-- Навигация -->
    <header>
        <div class="header">
        <!-- Логотип -->
            <div id="logo">
            <a href="index.html">
                <img src="img/logo.jpg" alt="logo">
            </a>
        </div>
        <div id="logo_name">Clo<br>Designer</div>
        
        
        <!-- Меню -->
        <ul id="menu">
            <li class="menu_main">
                <a href="index.html">
                    <p>Главная</p>
                </a>
            </li>
            <li class="menu_catalog">
                <a href="catalog.html">
                    <p>Каталог</p>
                    </a>
                <!-- <ul>
                    <li class="menu_catalog menu_catalog_item">
                        <a href="catalog/jacket.html">
                            <p>Косуха</p>
                        </a>
                    </li>
                    <li class="menu_catalog menu_catalog_item">
                        <a href="catalog/red_dress.html">
                            <p>Вечернее платье</p>
                            </a>
                    </li>
                    <li class="menu_catalog menu_catalog_item">
                        <a href="catalog/blue_dress.html">
                            <p>Замшевое платье</p>
                        </a>
                    </li>
                </ul> -->
            </li>
            <li class="menu_contacts">
                <a href="contacts.html">
                    <p>Контакты</p>
                </a>
            </li>
        </ul>
        </div>
    </header>
    

    <!-- Обертка, чтобы основная часть
    не пересекалась с header и footer -->
    <div id="wrap">
        <!-- Основная часть -->
        <main class="main">
            <div class="main_index">
                <h1>Clo Designer</h1>
                <h2>Магазин Дизайнеры одежды</h2>

                <div class="main_index_image_box">
                    <a href="catalog.html">
                        <img id="slider" src="img/main_image.jpg" alt="Постер главной страницы" >
                    </a>
                </div>
                <div class="loading_box">
                    <div id="loading"></div>
                </div>
                <button onclick="prev()"></button>
                <button onclick="next()"></button>

                <p>Добропозаловать на страницу нашего интернет магазина.<br>
                    Рады, что посетили наш портал.<br>
                Приятного вам времяпрепровождения.</p>
            </div>
        </main>
    </div>
    
    <div class="contacts_address">
            <h3>Как нас найти</h3>
        <p>Наш адрес: <b><i>Милан, Ломбардия, Италия</i></b><br>
        45.469157, 9.181438</p>
        <p><a href="mailto:yandex@yandex.ru">Написать нам.</a></p>
        <iframe id="map" src="https://yandex.ru/map-widget/v1/?um=constructor%3A58a23f1b93cb89ed86956ba6b1ac5eb93499e4ba30a3035ff73bfa916fc29f8f&amp;source=constructor"></iframe>
    </div>



    <!--  Футер -->
    <footer>
        <div class="footer">
            <div id="footer_info">
                <p>
                Disign by Aireend.<br>Link - 
                <a href="https://vk.com" target="_blank">
                    <img src="img/vk.png" alt="Ссылка VK" height="20"></a>
                <a href="https://www.instagram.com" target="_blank">
                    <img src="img/instagram.png" alt="Ссылка instagram" height="20"></a>
                </p>
            </div>
            <div id="all_rights_protections">Все права защищены.&nbsp;&copy;&nbsp;2017</div>
        </div>
    </footer>
</body>

</html>'''