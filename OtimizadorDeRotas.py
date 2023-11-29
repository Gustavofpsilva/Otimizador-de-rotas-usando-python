import googlemaps
from datetime import datetime

def otimizar_rotas(api_key, lugares):
    gmaps = googlemaps.Client(key=api_key)

    # Obtenha a matriz de distâncias e tempos de viagem entre os lugares
    matrix = gmaps.distance_matrix(origins=lugares, destinations=lugares, mode="driving")

    # Extraia a lista de destinos ordenados pela distância
    destinos_ordenados = [lugares[i] for i in matrix['rows'][0]['elements']]
    
    return destinos_ordenados

def main():
    # Substitua "SUA_CHAVE_DE_API" pela sua chave de API do Google Cloud Platform
    api_key = "SUA_CHAVE_DE_API"

    # Substitua os locais pelos seus destinos
    lugares = ["Endereço 1", "Endereço 2", "Endereço 3", "Endereço 4"]

    destinos_ordenados = otimizar_rotas(api_key, lugares)

    print("Ordem otimizada dos destinos:")
    for i, destino in enumerate(destinos_ordenados):
        print(f"{i+1}. {destino}")

if __name__ == "__main__":
    main()
