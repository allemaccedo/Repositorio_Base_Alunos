import flask, psycopg2, psycopg2.extensions, select
from flask import render_template, request, jsonify

app = flask.Flask(__name__)

def stream_messages(channel):
    conn= psycopg2.connect(database='postgres', user='postgres',
                           password='1234', host='localhost')
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

    curs = conn.cursor()
    curs.execute("LISTEN channel_%d;" % int(channel))

    while True:
        select.select([conn], [], [])
        conn.poll()
        while conn.notifies:
            notify = conn.notifies.pop()
            yield "data" + notify.payload + "\n\n"

@app.route("/message/<channel>", methods=['GET'])
def get_messages(channel):
    return flask.Response(stream_messages(channel), mimetype='text/event-stream')

@app.route("/message/new", methods=['POST'])
def new_messages():
    canal = request.args['channel']
    fonte = request.args['source']
    msg = request.args['message']

    try:
        conn = psycopg2.connect(database='postgres', user='postgres',
                           password='1234', host='localhost')
        
        curs = conn.cursor()
        curs.execute("INSERT INTO message(channel, source, content) VALUES(%s, %s, %s)", (canal,fonte,msg))
        conn.commit()
        conn.close()
        return jsonify({'message:': 'Conteudo enviado com sucesso'}, 500)
    except ConnectionRefusedError as e:
        print('Erro de conexão:', e)
        return jsonify({'error:': f'Erro de servidor: {e}'},500)

@app.route("/", methods=['GET','POST'])
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()