from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb://test:test@localhost', 27017)
# client = MongoClient('localhost', 27017)
db = client.hungryagri


##HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/harvest2')
def harvest():
    return render_template('harvest.html')


@app.route('/recipe2')
def recipe():
    return render_template('recipe.html')


##API 역할을 하는 부분
# 레시피 저장기능
@app.route('/recipe', methods=['POST'])
def save_recipe():
    name_receive = request.form['name_give']
    title_receive = request.form['title_give']
    review_receive = request.form['review_give']
    image_receive = request.form['image_give']
    doc = {
        'name': name_receive,
        'title': title_receive,
        'review': review_receive,
        'image': image_receive

    }

    db.recipe.insert_one(doc)

    return jsonify({'result': 'success', 'msg': '저장 완료!'})


# 레시피 목록보기
@app.route('/recipe', methods=['GET'])
def view_recipe():
    lists = list(db.recipe.find({}, {'_id': False}))
    return jsonify({'all_lists': lists})


# 텃밭 데이터 조회
@app.route('/harvest', methods=['GET'])
def show_info():
    info = list(db.moduga.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'all_infos': info})


# 검색 기능 구현


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
