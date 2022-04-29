# python-daz-test
> Script desafio: exportar múltiplas poses de múltiplas cenas DAZ
---
## Como Rodar
O script python pode recebe os seguintes parâmetros:
| Função | Descrição |
| ------ | ------ |
| custom_scene_dir | Altera o diretório que serão pegas as cenas |
| single_scene | Exporta as expressões de um arquivo único |
| output_dir | Modifica o caminho de output das poses exportadas |

Possíveis maneiras de rodar:
```sh
    python3.10 export_face_from_scene.py
```

Alterando o diretório de saída
```sh
    python3.10 export_face_from_scene.py -out "C:\Users\pedro.vasconcelos\Documents"
```

Alterando o diretório das cenas e de saída
```sh
    python3.10 export_face_from_scene.py --custom_scene_dir "C:\Users\pedro.vasconcelos\Documents\DAZ 3D\Studio\My Library\Scenes" -out "C:\Users\pedro.vasconcelos\Documents"
```

Convertendo uma única cena
```sh
    python3.10 export_face_from_scene.py --single_scene "C:\Users\pedro.vasconcelos\Documents\DAZ 3D\Studio\My Library\Scenes\boca_aberta_1.duf"
```