import json
import os


def config(filename="config.json"):

    # Obtém o diretório do script atual
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define o caminho para salvar: uma pasta acima do script e dentro de "config/"
    save_dir = os.path.join(os.path.dirname(script_dir), "config")

    # Caminho completo do arquivo JSON
    file_path = os.path.join(save_dir, filename)

    # Lê o JSON existente
    with open(file_path, 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)


def stepComplete(step, id):
    """
    Indica a conclusão de uma etapa específica em um processo.

    Parâmetros:
        step (str): Etapa concluída. Deve ser um dos seguintes valores:
            - "narration_complete"
            - "history_complete"
            - "video_complete"
            - "maker_complete"
            - "youtube_complete"
        id (str): Identificador que segue o padrão "<string>_<int>", onde:
            - A parte antes do underline (_) é uma string descritiva.
            - A parte após o underline (_) é um número inteiro representado como string.

    Retorna:
        None

    Exceções:
        ValueError: Se o parâmetro 'step' não estiver entre os valores permitidos ou se 'id' não seguir o padrão "<string>_<int>".
    """
    PATH_CONFIG = config()

    with open(PATH_CONFIG["historic_history"], 'r', encoding='utf-8') as arquivo:
        data = json.load(arquivo)
    
    temp = []
    temp = data[step]
    temp.append(id)
    data[step] = temp

    try:       
        
    
        with open(PATH_CONFIG["historic_history"], "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)

        print(f"✅ ✅ ✅ STEP: {step} - ID-VIDEO: {id} Complete! ✅ ✅ ✅ ")

    except:
        print(f"❌ ❌ ❌ STEP: {step} - ID-VIDEO: {id} Fail!  ❌ ❌ ❌ ")


def statusProdution(path):

    PATH_CONFIG = config()

    checkVideos(path)

    with open(PATH_CONFIG["historic_history"], 'r', encoding='utf-8') as arquivo:
        data = json.load(arquivo)


    titulo_pendentes = []
    titulo_fila = []
    titulo_completo = []

    total_titulos = 0
    id_gen = []
    id_titulo = []
    print("Todos os Temas - Licoes:-----------------------")
    for i in data['conteudo']:
        total_titulos = total_titulos + len(data['conteudo'][i]["theme"])
        for j in range(len(data['conteudo'][i]["theme"])):
            id_val = str(i)+"_"+str(j)
            id_gen.append(id_val)
            titulos_val = f"ID_VIODE: {id_val}    {data['conteudo'][i]['theme'][j]} - {data['conteudo'][i]['lesson'][j]}"
            id_titulo.append(titulos_val)
            print(titulos_val)
    
    
    print(f"❌Todos os Temas - Licoes PENDETES:-----------------------")
    for index, val in enumerate(id_gen):
        flag_nar = False
        flag_vid = False
        flag_his = False
        flag_you = False
        flag_mak = False

        if val in data['narration_complete']:
            flag_nar = True
        if val in data['history_complete']:
            flag_his = True
        if val in data['video_complete']:
            flag_vid = True
        if val in data['maker_complete']:
            flag_mak = True
        if val in data['youtube_complete']:
            flag_you = True

        if flag_nar and flag_vid and flag_his and flag_you and flag_mak:
            titulo_completo.append(id_titulo[index])
        if (flag_nar or flag_vid or flag_his or flag_you or flag_mak) and val not in titulo_completo:
            titulo_pendentes.append(id_titulo[index])

            print(titulos_val)
            print(f"Pendete: Narração({flag_nar}), Historia({flag_his}), Video({flag_vid}), Maker({flag_mak}), Youtube({flag_you})")



    print(f"❌Todos os Temas - Licoes FILA:-----------------------")
    for i in titulo_pendentes:
        print(i)

    print(f"✅Todos os Temas - Licoes COMPLETOS:-----------------------")
    for i in titulo_completo:
        print(i)

def checkVideos(path):
    PATH_CONFIG = config()

    with open(PATH_CONFIG["historic_history"], 'r', encoding='utf-8') as arquivo:
        data = json.load(arquivo)

    lista_videos = {}
    for i in os.listdir(config["path_video"]):
        split = i.split("_")
        id = split[0] + "_"+split[0]

        if split[0] in data['conteudo']:
            lista_videos[id]["total"] = len(data['conteudo'][split[0]]['theme'])
            try:
                lista_videos[id]["count"] = lista_videos[id]["count"] + 1
            except:
                lista_videos[id]["count"] = 1

    for i in lista_videos:
        if lista_videos[i]["total"] == lista_videos[i]["count"]:
            if i not in  data['video_complete']:
                aux = data['video_complete']
                aux.append(i)
                data['video_complete'] = aux
                with open(PATH_CONFIG["historic_history"], "w", encoding="utf-8") as json_file:
                    json.dump(data, json_file, indent=4, ensure_ascii=False)


    print(f"✅ Lista de Video atualizado")
            

            
if __name__ == "__main__":
    statusProdution()
    


