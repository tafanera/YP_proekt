
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey'

user_db = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    if username in user_db:
        return 'Пользователь уже существует', 400
    user_db[username] = password
    session['username'] = username
    return redirect(url_for('artists'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if user_db.get(username) != password:
            return 'Неверный логин или пароль', 401
        session['username'] = username
        return redirect(url_for('artists'))
    return render_template('login.html')

@app.route('/registr')
def registr():
    return render_template('registr.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/artists')
def artists():
    return render_template('artists.html')

@app.route('/artist/<int:artist_id>')
def artist(artist_id):
    artist_info = {'id': artist_id, 'name': f'Artist {artist_id}'}
    return render_template('artist.html', artist=artist_info)

@app.route('/rate_artist', methods=['POST'])
def rate_artist():
    if 'username' not in session:
        return jsonify({'success': False}), 403

    data = request.get_json()
    review = {
        'id': int(datetime.now().timestamp()),
        'user_id': session['username'],
        'artist_id': data['artist_id'],
        'rating': int(data['rating']),
        'comment': '',
        'created_at': datetime.utcnow().isoformat() + 'Z'
    }

    try:
        with open('reviews.json', 'r', encoding='utf-8') as f:
            reviews = json.load(f)
    except:
        reviews = []

    reviews.append(review)

    with open('reviews.json', 'w', encoding='utf-8') as f:
        json.dump(reviews, f, ensure_ascii=False, indent=2)

    return jsonify({'success': True})

@app.route('/mayot')
def mayot():
    artist_info = {
        'id': 1,
        'name': ' MAYOT',
        'image_url': url_for('static', filename='images/mayot2.jpg'),
        'yandex_links': [
            'https://music.yandex.ru/album/33398863?utm_source=desktop&utm_medium=copy_link',
            'https://music.yandex.ru/album/26762937?utm_source=desktop&utm_medium=copy_link',
            'https://music.yandex.ru/album/24383585?utm_source=desktop&utm_medium=copy_link',
            'https://music.yandex.ru/album/22810726?utm_source=desktop&utm_medium=copy_link',
            'https://music.yandex.ru/album/14562740?utm_source=desktop&utm_medium=copy_link',
            'https://music.yandex.ru/album/11828535?utm_source=desktop&utm_medium=copy_link',
        ],
        'yandex_images': [
            'zp4d.jpg', 'oba.jpg', 'zp3.jpg',
            'scum.jpg', 'zp2.jpg', 'ghetto.jpg'
        ],
        'youtube_links': [
            'https://youtu.be/EdUtO1BaZM8?si=G8bnEl9jz6js5x3l',
            'https://youtu.be/SNz5H1PnE1E?si=CS7dEFBtspIGe0sc',
            'https://youtu.be/saLG2KSU82I?si=bQXwkGrY8ReM9_Pz',
            'https://youtu.be/CNGE3sFBjys?si=0CH-cJf-5SpII0e6',
            'https://youtu.be/aqKuKy29lD0?si=fxoueeugG1A-5be1',
            'https://youtu.be/jlZ8MW4nYl0?si=dlIkHW4lJzdeNEv9',
        ],
        'youtube_images': [
            'mklip.jpg', 'mklip1.jpg', 'mklip2.jpg',
            'mklip3.jpg', 'mklip4.jpg', 'mklip5.jpg'
        ]
    }
    return render_template('mayot.html', artist=artist_info)

@app.route('/water')
def water():
    artist_info = {
        'id': 1,
        'name': 'HERONWATER',
        'image_url': url_for('static', filename='images/waterr.jpg'),
        'yandex_links': [
            'https://music.yandex.ru/album/33981793?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/27558962?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/24203702?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/22634923?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/26221804?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/29758238?utm_source=web&utm_medium=copy_link',
        ],
        'yandex_images': [
            'odysey.jpg', 'dreams.jpg', 'lyric.jpg',
            '2day.jpg', 'posmotret.jpg', '4m.jpg'
        ],
        'youtube_links': [
            'https://youtu.be/pnATM4kFJFU?si=P2VB-BwW-XFmGhJa',
            'https://youtu.be/llZ3JsfR50o?si=9SiSWwZADCvYHJ78',
            'https://youtu.be/1WUrR53i37Q?si=P_u7wpS6LF4sIULR',
            'https://youtu.be/p7T4Bkdxh3s?si=pgRAF6p_HS3nyEBv',
            'https://youtu.be/FfDpVZRD2Tk?si=vfpip-zdZM15ucBL',
            'https://youtu.be/QWmiFsAILYg?si=FrNn9_NrhyVS13zj',
        ],
        'youtube_images': [
            '1st.jpg', 'zavisim.jpg', 'svarovski.jpg',
            'tokyo.jpg', 'beast.jpg', 'star.jpg'
        ]
    }
    return render_template('water.html', artist=artist_info)

@app.route('/obla')
def obla():
    artist_info = {
        'id': 1,
        'name': 'OBLADAET',
        'image_url': url_for('static', filename='images/oblad.jpg'),
        'yandex_links': [
            'https://music.yandex.ru/album/35707084?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/28150967?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/14407003?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/9004297?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/6177175?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/4321538?utm_source=web&utm_medium=copy_link',
        ],
        'yandex_images': [
            '735.png', 'pc2.jpg', 'ps.jpg',
            '3d.jpg', 'ice.jpg', 'files.jpg'
        ],
        'youtube_links': [
            'https://youtu.be/qZZV6VhVULI?si=JwexRrSxoTjvZ_4v',
            'https://youtu.be/k9bxe2c8Lxs?si=4R0aQqOc0AJKF06f',
            'https://youtu.be/1sXwnFtir_Y?si=ZPI1ZdbaSfp0o6Gs',
            'https://youtu.be/jVYSc3H-DQM?si=784MULKRb9fW7Cr9',
            'https://youtu.be/sFG_1BkjmTw?si=R3U7MAsNPajfQmVG',
            'https://youtu.be/xfi3N92VBiI?si=gjzwjz2czwtCXmxa',
        ],
        'youtube_images': [
            'wys.jpg', 'barman.jpg', 'ysm.jpg',
            'brith.jpg', 'boo.jpg', 'house.jpg'
        ]
    }
    return render_template('obla.html', artist=artist_info)

@app.route('/whl')
def whl():
    artist_info = {
        'id': 1,
        'name': 'Whole Lotta Swag',
        'image_url': url_for('static', filename='images/wholle.jpg'),
        'yandex_links': [
            'https://music.yandex.ru/album/35835727?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/30662581?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/27756795?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/25924897?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/24027607?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/32813260?utm_source=web&utm_medium=copy_link',
        ],
        'yandex_images': [
            'notype.jpg', 'newcoast.jpg', '68.jpg',
            'firma.jpg', 'press.jpg', 'okraina.jpg'
        ],
        'youtube_links': [
            'https://youtu.be/_4YT0KehgRU?si=oIQ_Y3Cfo3Bz1XWy',
            'https://youtu.be/cJwt_dQlts0?si=0wLPvj1GhxMepn1O',
            'https://youtu.be/TJh1Fbh7duw?si=XJZfAME3DWqR8Nps',
            'https://youtu.be/YG3Ba8s0Mzo?si=R7RQvgDFLtNcejDr',
            'https://youtu.be/_Jb_czObAvM?si=Q_ZlG5JrlGdL04L7',
            'https://youtu.be/xmE_8Y7Ofu4?si=D2doSg2PYHzgmKQX',
        ],
        'youtube_images': [
            'krizis.jpg', 'pododisuda.jpg', 'formalnost.jpg',
            'workal.jpg', 'okkraina.jpg', 'bigcity.jpg'
        ]
    }
    return render_template('whl.html', artist=artist_info)

@app.route('/august')
def august():
    artist_info = {
        'id': 1,
        'name': 'August',
        'image_url': url_for('static', filename='images/auggust.jpg'),
        'yandex_links': [
            'https://music.yandex.ru/album/35210606?utm_source=desktop&utm_medium=copy_link',
            'https://music.yandex.ru/album/28166086?utm_source=desktop&utm_medium=copy_link',
            'https://music.yandex.ru/album/23302438?utm_source=desktop&utm_medium=copy_link',
            'https://music.yandex.ru/album/16909106?utm_source=desktop&utm_medium=copy_link',
            'https://music.yandex.ru/album/36403360?utm_source=desktop&utm_medium=copy_link',
            'https://music.yandex.ru/album/33916433?utm_source=desktop&utm_medium=copy_link',
        ],
        'yandex_images': [
            'djaugust.png', 'night.jpg', '365.jpg',
            '5.jpg', 'town.jpg', 'tfest.jpg'
        ],
        'youtube_links': [
            'https://youtu.be/SLOEnfW5UFc?si=H8K7wqoTx5m7kv38',
            'https://youtu.be/F-k6or0z1FU?si=Wl2ZZHWwirQTFq2S',
            'https://youtu.be/o5KJouM1TSA?si=tf_gxYxAWkwUg5Vr',
            'https://youtu.be/K-bGyw38z2Y?si=4z3_2nRlxUr6_9fe',
            'https://youtu.be/k-nWyIeUj9c?si=PPD1nLsV71pPbiM0',
            'https://youtu.be/KRxsrA3V8JA?si=moQG0FBL4XNhu2xa',
        ],
        'youtube_images': [
            'riana.jpg', 'dlyatebya.jpg', 'club.jpg',
            'mybad.jpg', 'bkwd.jpg', 'wakeup.jpg'
        ]
    }
    return render_template('august.html', artist=artist_info)

@app.route('/lilk')
def lilk():
    artist_info = {
        'id': 1,
        'name': 'LIL KRYSTALLL',
        'image_url': url_for('static', filename='images/lilkk.jpg'),
        'yandex_links': [
            'https://music.yandex.ru/album/28464612?utm_source=desktop&utm_medium=copy_link',
            'https://music.yandex.ru/album/33073663?utm_source=desktop&utm_medium=copy_link',
            'https://music.yandex.ru/album/7179448?utm_source=desktop&utm_medium=copy_link',
            'https://music.yandex.ru/album/12639857?utm_source=desktop&utm_medium=copy_link',
            'https://music.yandex.ru/album/36450561?utm_source=desktop&utm_medium=copy_link',
            'https://music.yandex.ru/album/34604678?utm_source=desktop&utm_medium=copy_link',
        ],
        'yandex_images': [
            'kristina.jpg', 'no label.jpg', 'brat3.png',
            'lilkrystall.jpg', 'chrome.jpg', 'redflag.jpg'
        ],
        'youtube_links': [
            'https://youtu.be/W4EzkbMc5_M?si=5107oRyJ6mT1c7A6',
            'https://youtu.be/jAYvKxSx4qU?si=sMPWERtMv1cONSv6',
            'https://youtu.be/Mo1hidG4cgo?si=Y15ifhwsOYUs62up',
            'https://youtu.be/2tDlOm2gVM8?si=oeab7yFa7gcT7aLg',
            'https://youtu.be/k-nWyIeUj9c?si=PPD1nLsV71pPbiM0',
            'https://youtu.be/KRxsrA3V8JA?si=moQG0FBL4XNhu2xa',
        ],
        'youtube_images': [
            'kris.jpg', 'october.jpg', 'jack.jpg',
            'matilda.jpg', 'kykla.jpg', 'everyday.jpg'
        ]   
    }
    return render_template('lilk.html', artist=artist_info)

@app.route('/saluki')
def saluki():
    artist_info = {
        'id': 1,
        'name': 'SALUKI',
        'image_url': url_for('static', filename='images/saluk.jpg'),
        'yandex_links': [
            'https://music.yandex.ru/album/33932468?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/31807414?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/25511786?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/15104071?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/9337806?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/7697300?utm_source=web&utm_medium=copy_link',
        ],
        'yandex_images': [
            'kyrtki.jpg', 'hotel.jpg', 'wild.jpg',
            'slava.jpg', 'people.jpg', 'vlastelin.jpg'
        ],
        'youtube_links': [
            'https://youtu.be/OB38tTXHqNA?si=nhKuU_1F5ZU9g9d3',
            'https://youtu.be/jCE34DMLBRQ?si=IbJ3xjzpIxzsDcCy',
            'https://youtu.be/gaxPqUW1JfU?si=hSH5xuWXRcc6y5A9',
            'https://youtu.be/H6tNm72cMA8?si=Lq_DRiXDSDkdjj38',
            'https://youtu.be/rdoSb5GOhNQ?si=LLhRxkxsDkpmQmtv',
            'https://youtu.be/DdaNFvq_Kxs?si=aDmOKvCmzLvYT5er',
        ],
        'youtube_images': [
            'hotel2.jpg', 'toxis.jpg', 'vedma.jpg',
            'ogney.jpg', 'hahaha.jpg', 'vent.jpg'
        ]
    }
    return render_template('saluki.html', artist=artist_info)

@app.route('/soda')
def soda():
    artist_info = {
        'id': 1,
        'name': 'SODA LUV',
        'image_url': url_for('static', filename='images/sodd.jpg'),
        'yandex_links': [
            'https://music.yandex.ru/album/36043067?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/31497207?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/28211323?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/25381044?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/22749010?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/20131597?utm_source=web&utm_medium=copy_link',
        ],
        'yandex_images': [
            'idio.jpg', 'sodaluv.jpg', 'spa.jpg',
            'nl2.jpg', 'ns.jpg', 'room.jpg'
        ],
        'youtube_links': [
            'https://youtu.be/hi5Quy4tINo?si=43_antjVdSpSF4ji',
            'https://youtu.be/A5BAN3mSpvM?si=-3jc1nkwEz1sgT-O',
            'https://youtu.be/U5iqHWJdZY8?si=Wrwv3ENCw8R6GH9D',
            'https://youtu.be/6Ll0wVehTHY?si=1cEC2GQ20eYI-vkH',
            'https://youtu.be/64_7295piLg?si=JqdsXDfQRA34ryll',
            'https://youtu.be/ZMZdCQY8_ZQ?si=oHWRwvTfu59XtTUG',
        ],
        'youtube_images': [
            'kopi.jpg', 'daleko.jpg', 'maybach.jpg',
            'sorbet.jpg', 'cole.jpg', 'dim.jpg'
        ]
    }
    return render_template('soda.html', artist=artist_info)

@app.route('/tgug')
def tgug():
    artist_info = {
        'id': 1,
        'name': 'FRIENDLY THUG 52 NGG',
        'image_url': url_for('static', filename='images/tug.jpg'),
        'yandex_links': [
            'https://music.yandex.ru/album/36376575?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/28026987?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/22172320?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/32844001?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/31461919?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/22955871?utm_source=web&utm_medium=copy_link',
        ],
        'yandex_images': [
            'graf.jpg', 'colomb.jpg', 'aurora.jpg',
            'lager.jpg', 'ammo.jpg', 'struglle.jpg'
        ],
        'youtube_links': [
            'https://youtu.be/dj1V8RnuYcw?si=WgrPiyOaatcm9-5Z',
            'https://youtu.be/8muZaiG4yU4?si=LH7qN6FGaCGVflbG',
            'https://youtu.be/99r1Yids9z0?si=-ZIpJQMSl4s60Pc4',
            'https://youtu.be/TIYgqUlZ3L4?si=1L65691r6uXlx-T9',
            'https://youtu.be/UsiBGEGCPVA?si=McYfMyxYVZSJtv3x',
            'https://youtu.be/Hxe6tAG_B_U?si=6nSNe4Tmm1zSn7Hu',
        ],
        'youtube_images': [
            'am.jpg', 'la.jpg', 'son.jpg',
            'calmer.jpg', 'loyal.jpg', 'ffm.jpg'
        ]
    }
    return render_template('tgug.html', artist=artist_info)

@app.route('/fendi')
def fendi():
    artist_info = {
        'id': 1,
        'name': 'FENDIGLOCK',
        'image_url': url_for('static', filename='images/fennd.jpg'),
        'yandex_links': [
            'https://music.yandex.ru/album/35929507?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/32252131?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/27545639?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/25129938?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/22249217?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/18153844?utm_source=web&utm_medium=copy_link',
        ],
        'yandex_images': [
            'not.jpg', 'oxana.jpg', 'trend.jpg',
            'pill.jpg', 'fendik.jpg', 'exs.jpg'
        ],
        'youtube_links': [
            'https://youtu.be/PDppdDCoei4?si=XP47H-y0ELsN7RgZ',
            'https://youtu.be/m2lt5PmQgUw?si=Qf_D25JyE5ejU9pg',
            'https://youtu.be/ItPuoWTGzLg?si=GwzNC5hG4N-MbR89',
            'https://youtu.be/RB9XSl529gQ?si=zSbZ8I2Aw_D2ClGf',
            'https://youtu.be/o9xi-8bVYpA?si=kRLpQ2Mae3oAYkBc',
            'https://youtu.be/ZZkgYOONjjA?si=xp9flJwq27dFtHYJ',
        ],
        'youtube_images': [
            'zombe.jpg', 'lobotomiya.jpg', 'luchshe.jpg',
            'doping.jpg', 'farm.jpg', 'minervius.jpg'
        ]
    }
    return render_template('fendi.html', artist=artist_info)

@app.route('/platina')
def platina():
    artist_info = {
        'id': 1,
        'name': 'Платина',
        'image_url': url_for('static', filename='images/robchik.jpg'),
        'yandex_links': [
            'https://music.yandex.ru/album/30549757?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/17444119?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/33069734?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/33079053?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/34551521?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/36327582?utm_source=web&utm_medium=copy_link',
        ],
        'yandex_images': [
            'platin.jpg', 'sosa.jpg', 'opiat.jpg',
            'sni.jpg', 'rnb.jpg', 'neo.jpg'
        ],
        'youtube_links': [
            'https://youtu.be/IFTUkfcTvZM?si=jxWBdHoK0ct104H-',
            'https://youtu.be/iObYN_So_5I?si=M8gQrzDgiiXN7cXh',
            'https://youtu.be/OC_sNsFzGqg?si=8NLT1-cIXE8OxY9U',
            'https://youtu.be/b2re-rj0izY?si=jCYilQ3dNacwOd99',
            'https://youtu.be/Tdlqxue8-UM?si=yPdfsZnrNrFLQkYn',
            'https://youtu.be/maDrQPge89g?si=JkSeAjwVFNqAYtF-',
        ],
        'youtube_images': [
            'neoo.jpg', 'poveril.jpg', 'zaviduyt.jpg',
            'valina.jpg', 'liga.jpg', 'santa.jpg'
        ]
    }
    return render_template('platina.html', artist=artist_info)

@app.route('/tape')
def tape():
    artist_info = {
        'id': 1,
        'name': 'Big Baby Tape',
        'image_url': url_for('static', filename='images/tappe.jpg'),
        'yandex_links': [
            'https://music.yandex.ru/album/31785098?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/28255531?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/18861051?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/7456110?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/6072366?utm_source=web&utm_medium=copy_link',
            'https://music.yandex.ru/album/6097953?utm_source=web&utm_medium=copy_link',
        ],
        'yandex_images': [
            'peekaboo.jpg', 'varskva.jpg', 'bandana.jpg',
            'argument.jpg', 'dragonborn.jpg', 'hoodrich.jpg'
        ],
        'youtube_links': [
            'https://youtu.be/_61BkXti1_Q?si=tK-dJVCjz8rQjHGr',
            'https://youtu.be/c8Ctwtj3Bgk?si=3BQBxL6AJByQPmPg',
            'https://youtu.be/qXoRx4rmUcE?si=RqKXYMOUSI4wmGQn',
            'https://youtu.be/BnxTfeEIP_Y?si=m0Cb0UT0bTthPUdx',
            'https://youtu.be/Z7SSLzPeIHg?si=sNwMQ61zPQUFQaNy',
            'https://youtu.be/lCEbUucGiZ8?si=Az1VXazOuU76anhH',
        ],
        'youtube_images': [
            'turbo.jpg', 'diddy.jpg', 'siento.jpg',
            'bent.jpg', 'obama.jpg', 'nihao.jpg'
        ]
    }
    return render_template('tape.html', artist=artist_info)


if __name__ == '__main__':
    app.run(debug=True)

