from ollama import Client
import json
import os
import regex as re
from tqdm import tqdm
import argparse
from .utils.setup import config


def safeTextUnicodeYoutube(texto):
    # Substitui aspas duplas por uma string vazia
    texto_sem_aspas = texto.replace('"', '')
    # Substitui quebras de linha por uma string vazia
    texto_limpo = texto_sem_aspas.replace('\n', '')
    return texto_limpo

def safeTextUnicodeSpeak(texto):
    # Substitui caracteres que não sejam letras, vírgulas, pontos de interrogação, pontos de exclamação ou espaços
    return re.sub(r'[^\p{L},¡¿!? ]+', '', texto) 

def safeTextUnicodeScene(texto):
    # Substitui caracteres que não sejam letras, vírgulas, pontos de interrogação, pontos de exclamação ou espaços
    return re.sub(r'[^\p{L},¡¿!? .:]+', '', texto) 


def formatPromptYoutube(history, tema, licao):
    """
    Gera o prompt para criação de conteúdo para YouTube baseado na história infantil.

    Parâmetros:
        history (str): A história infantil completa.
        tema (str): O tema utilizado para gerar a história.
        licao (str): A lição ou moral da história.

    Retorna:
        str: Um prompt formatado que solicita a geração de título, descrição e tags 
             para o vídeo no YouTube, estruturado em JSON.
    """
    return "Considere a história infantil: "+ history +". Gerado pelo tema '"+ tema + "' com a lição da história '" + licao + """'
    Gere para o youtube:

    [title] Um ótimo título incrível para história.
     
    [description] Também gere uma ótima descrição.
    
    [tags] Gere ótimas tag/palavras chaves no formato "tag, tag, tag,..." para youtube, ou seja, apenas as palavras chaves separado por virgula com máximo de 400 caracteres, elabore para vídeo no YouTube, adicione ícones interessantes sobre o tema, hashtag na descrição.

    responda apenas em texto extritamente nesta estrutura JSON:

    {
        "title": "....",
        "tags": ["tag1","tag2",...],
        "description":"..."    

    }"""


def formatPromptNarracao(tema, licao):
    """
    Gera o prompt para criação de uma história infantil narrada.

    Parâmetros:
        tema (str): O tema da história.
        licao (str): A lição ou moral da história.

    Retorna:
        str: Um prompt formatado que solicita a geração de uma narração da história,
             com frases de aproximadamente 120 caracteres cada e cerca de 12 frases, 
             estruturado em JSON.
    """
    return """
    
    Gere uma história infantil com o tema " 
    
    
    """ + tema + """ 
    
    " com a lição da história " 
    
    
    """ + licao + """ 
    
    " . Quero o formato da seguinte forma:

    [narration] Narração frase a frase de aproximadamente 120 caracteres, e aproximadamente 12 frases.
    responda apenas como texto extritamente nesta estrutura JSON:

    {
        "narration":[ "frase1 ....", "frase2 ...", ...]

    }"""

def formatPromptDescriptionScenes(scene,history,person):
    """
    Gera o prompt para a descrição de uma cena específica da história infantil.

    Parâmetros:
        scene (str): A parte ou frase da narração que descreve a cena.
        history (str): A história completa, utilizada para fornecer contexto.
        person (str): A descrição do personagem principal que deverá ser incorporada na cena.

    Retorna:
        str: Um prompt formatado que solicita a geração de uma descrição resumida da cena 
             (aproximadamente 100 caracteres), enfatizando o cenário, os personagens e suas ações.
    """
    return "Considerando a historia "+ history+ ". Focando apenas nesse trecho '"+ scene +"'." + """""' 

    [scenes] Gerar uma descrição da cena, descrevendo um cenário incrível com personagens e suas ações e o ambiente/local onde se passa a cena, importante, substitua a menção do personagem esse texto: '
    
    """+ person +"""

    '
    
    , e repita a descrição dos personagens em todas as cenas. Resuma em aproximadamente 100 caracteres

    responda apenas como texto extritamente:

    "...."


    """

def formatPromptDescriptionPerson(history):
    """
    Gera o prompt para a descrição completa do personagem principal da história.

    Parâmetros:
        history (str): A história completa, que servirá de base para a descrição do personagem.

    Retorna:
        str: Um prompt formatado que solicita uma descrição resumida e completa do personagem principal,
             incluindo detalhes como vestimenta e aparência.
    """
    return "Considerando a historia '"+ history+ """

    ' Gere uma descrição completa do personagem principal, como o que veste, sua aparência, resuma.
    responda apenas no formato texto extritamente:

    "...."


    """

def formatPromptTranslate(conteudo, idioma):
    """
    Gera o prompt para tradução de um conteúdo para o idioma especificado.

    Parâmetros:
        conteudo (str): O texto que deverá ser traduzido.
        idioma (str): O idioma para o qual o conteúdo deverá ser traduzido.

    Retorna:
        str: Um prompt formatado que solicita a tradução do conteúdo, respondida apenas como TEXT.
    """
    return "Traduza para a lingua '"+ idioma+ """

    ' o conteudo:

    "
    """+ conteudo +"""
    "

    Responda apenas no formato texto.

    """

def sendPrompt(prompt):
    """
    Envia o prompt para o serviço de chat utilizando o Client da biblioteca 'ollama' e retorna a resposta.

    Parâmetros:
        prompt (str): O prompt a ser enviado para o modelo de chat.

    Retorna:
        str: A resposta do modelo, com formatações indesejadas (como marcação de JSON) removidas, se necessário.
    """
       
    # print("Prompt:", prompt)
    client = Client(
    host='http://127.0.0.1:11434/',
    headers={'x-some-header': 'some-value'}
    )
    response = client.chat(model='gemma3', messages=[
    {
        'role': 'user',
        'content': prompt,
    },
    ])

    resposta = response.message.content
    if "json" in resposta:
        resposta = (response.message.content).replace("```json","")
        resposta = resposta.replace("```","")
    return resposta


def create_storys(temas, licoes):

    """
    Função principal que orquestra a criação, tradução e armazenamento de uma história infantil.

    O fluxo de execução é o seguinte:
      1. Seleciona um índice (exemplo: i = 10) e gera a narração da história utilizando 'formatPromptNarracao'.
      2. Processa a resposta JSON para extrair a narração e gera, para cada frase, uma descrição de cena usando 'formatPromptDescriptionScenes'.
      3. Gera o prompt para criação do conteúdo para YouTube com 'formatPromptYoutube' e processa a resposta JSON.
      4. Realiza traduções para múltiplos idiomas (lista de idiomas e siglas definidas) para título, tags, descrição, narração e (para inglês) cenas utilizando 'formatPromptTranslate'.
      5. Armazena o resultado final em um arquivo JSON no caminho especificado.

    Parâmetros:
        temas (list): Lista de temas para a geração de histórias.
        licoes (list): Lista de lições correspondentes aos temas.

    Retorna:
        (None)
        SAVE PATH_HISTORY:
        "lan" = {
        "title": "....",
        "scenes": ["scenes1","scenes2",...,"scenes N"],
        "narration": ["narration1","narration2",...,"narration N"],
        "tags": ["tag1","tag2",...],
        "description":"..."    

        }
    """

    print("Carregando configs!")

    # Obtém o diretório do script atual
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define o caminho para salvar: uma pasta acima do script e dentro de "config/"
    file_path = os.path.join(script_dir, "config", "config.json")

    if file_path :
        # Lê o JSON existente
        with open(file_path, 'r', encoding='utf-8') as arquivo:
            config = json.load(arquivo)
    else:
        print("Erro config não existe")
    resposta = sendPrompt(formatPromptNarracao(temas, licoes))
    try:
        dados_json = json.loads(resposta)
        narracao = dados_json['narration']

        narracao_safe = []
        for safenarration in narracao:
            narracao_safe.append(safeTextUnicodeSpeak(safenarration)+ ", ")
        narracao = narracao_safe

        dados_json['narration'] = narracao
        scenes = []
        history = "".join(narracao)
        for scene in narracao:
            resposta_scene = sendPrompt(formatPromptDescriptionScenes(scene, history, formatPromptDescriptionPerson(history)))
            scenes.append(safeTextUnicodeScene(resposta_scene))
        
        resposta_youtube = sendPrompt(formatPromptYoutube(history, temas, licoes))
        try:
            dados_json_final = json.loads(resposta_youtube)

            dados_json_final["title"] = safeTextUnicodeYoutube(dados_json_final["title"]) 
            dados_json_final["tags"] = safeTextUnicodeYoutube(dados_json_final["tags"]) 
            dados_json_final["description"] = safeTextUnicodeYoutube(dados_json_final["description"]) 
            dados_json_final["narration"]=narracao
            dados_json_final["scenes"]=scenes
            
        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar JSON: {e}")
            print(f"Conteúdo da resposta: {resposta_youtube}")
        
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")
        print(f"Conteúdo da resposta: {resposta_scene}")

    languages = ["árabe","inglês", "espanhol", "francês", "alemão", "italiano", "polonês", "turco", "russo", "holandês", "tcheco", "chinês", "japonês", "húngaro", "coreano", "hindi"]
    siglas = ["ar", "en", "es", "fr", "de", "it", "pl", "tr", "ru", "nl", "cs",  "zh-cn", "ja", "hu", "ko", "hi"]
    dados_multlanguage = {}
    dados_multlanguage["pt"] = dados_json_final
    for j in tqdm(range(len(languages))):
        temp = {}
        resposta_lang = sendPrompt(formatPromptTranslate(dados_json_final["title"], languages[j]))
        temp['title'] = safeTextUnicodeYoutube(resposta_lang)
        resposta_lang = sendPrompt(formatPromptTranslate(dados_json_final["tags"], languages[j]))
        temp['tags'] = safeTextUnicodeYoutube(resposta_lang)
        resposta_lang = sendPrompt(formatPromptTranslate(dados_json_final["description"], languages[j]))
        temp['description'] = safeTextUnicodeYoutube(resposta_lang)
        aux = []
        for n in dados_json_final["narration"]:
            resposta_lang = sendPrompt(formatPromptTranslate(n, languages[j]))
            aux.append(safeTextUnicodeSpeak(resposta_lang)+ ", ")
        temp['narration'] = aux
        aux = []
        if siglas[j] == "en":
            for n in dados_json_final["scenes"]:
                resposta_lang = sendPrompt(formatPromptTranslate(n, languages[j]))
                aux.append(safeTextUnicodeScene(resposta_lang))
            temp['scenes'] = aux
        dados_multlanguage[siglas[j]] = temp     
            
    
    with open(config["path_history"]+str(i)+"_history.json", 'w', encoding='utf-8') as f:
                json.dump(dados_multlanguage, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":




    print("Iniciando Narração .....")
    parser = argparse.ArgumentParser(description="Configurações e input do id da historia")
    parser.add_argument("theme", type=str, help="ID da historia a qual será gerada as narrações")
    parser.add_argument("lesson", type=str, help="ID da historia a qual será gerada as narrações")
    parser.add_argument("--config", type=bool, help="Idade da pessoa", default=False)

    args = parser.parse_args()
    print(f"Theme: {args.theme}")
    print(f"Lesson: {args.lesson}")
    print(f"--config: {args.config}")

    if args.config :
        config()

    create_storys(args.theme, args.lesson)
        