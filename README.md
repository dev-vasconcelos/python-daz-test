# python-daz-test
> Script desafio: exportar múltiplas poses de várias cenas DAZ.

Observações:
> O script já exporta as poses para o formato .duf na pasta padrão de poses do DAZ.
> Foquei em deixar o script o mais "clicou rodou" possível
> Há a opção de alterar por parâmetro tanto o diretório de entrada de arquivos, quanto de saída.

---
## Arquivos
| Nome | Descrição |
| ------ | ------ |
| export_face_from_scene | Script principal, o que será rodado |
| test_file | Script para fazer pequenos testes antes de implementar no princpal |

## Como Rodar
O script python pode receber os seguintes parâmetros:
| Função | Descrição |
| ------ | ------ |
| custom_scene_dir | Altera o diretório que serão pegas as cenas |
| single_scene | Exporta as expressões de um arquivo único |
| output_dir | Modifica o caminho de output das poses exportadas |
## Possíveis maneiras de rodar:
Sem parâmetros, pegando cenas da pasta padrão do DAZ e lançando para a pasta de poses:
```sh
    python3.10 export_face_from_scene.py
```

Alterando o diretório de saída:
```sh
    python3.10 export_face_from_scene.py -out "C:\Users\pedro.vasconcelos\Documents"
```

Alterando o diretório das cenas e de saída:
```sh
    python3.10 export_face_from_scene.py --custom_scene_dir "C:\Users\pedro.vasconcelos\Documents\DAZ 3D\Studio\My Library\Scenes" -out "C:\Users\pedro.vasconcelos\Documents"
```

Convertendo uma única cena:
```sh
    python3.10 export_face_from_scene.py --single_scene "C:\Users\pedro.vasconcelos\Documents\DAZ 3D\Studio\My Library\Scenes\boca_aberta_1.duf"
```
