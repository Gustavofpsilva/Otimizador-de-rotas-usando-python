Otimização de Rotas com Google Maps API
Este script Python utiliza a API do Google Maps para otimizar a ordem de destinos em uma rota, considerando a distância de condução entre eles. O objetivo é reorganizar uma lista de lugares de forma a minimizar o tempo de viagem total.

Requisitos
Python 3.x
Biblioteca: googlemaps
Configuração Inicial
Obtenha uma chave de API do Google Cloud Platform.
Substitua "SUA_CHAVE_DE_API" pela chave obtida na etapa anterior.
Substitua os locais na lista lugares pelos destinos desejados.
Uso
Execute o script:

bash
Copy code
python seu_script.py
O script utiliza a API do Google Maps para obter a matriz de distâncias e tempos de viagem entre os lugares fornecidos.

A lista de destinos é reordenada com base na distância de condução, resultando em uma ordem otimizada.

A ordem otimizada dos destinos é exibida no console.

Observações
Chave de API: Certifique-se de que a chave de API do Google Cloud Platform esteja configurada corretamente.

Locais: Personalize a lista de lugares de acordo com seus destinos específicos.

Modo de Viagem: O script está configurado para otimizar rotas no modo de condução (mode="driving"). Se necessário, ajuste o modo conforme suas necessidades.

Licença
