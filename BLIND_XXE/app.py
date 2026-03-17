from flask import Flask , request
from lxml import etree

app = Flask(__name__)

@app.route('/process' , methods=['POST'])
def process_xml():
    xml_data = request.data
    if not xml_data:
        return "pls send POST content"
    try:
        parser = etree.XMLParser(resolve_entities=True, load_dtd=True, no_network=False)
        tree = etree.fromstring(xml_data ,parser)
        return "Sending Data successfully!" , 200
    except Exception as e:
        return "Error parsing" , 400
if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=5000)