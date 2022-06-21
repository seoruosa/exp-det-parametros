# Atividade 3 - Configuração automática de parâmetros

## Instalação
* Instalar [R](https://mlopez-ibanez.github.io/irace/#gnulinux)

    ``` sudo apt-get install r-base ```
* Instalar irace
    ``` 
        $ R
        R> install.packages("irace") 
    ```
    * Resolvendo problema com a instalação do pacote -> [link](https://stackoverflow.com/questions/32540919/library-is-not-writable)

* Adicionar o diretório do irace no [path](https://mlopez-ibanez.github.io/irace/#gnulinux-and-os-x):
    ```
        export IRACE_HOME=/path/to/R/irace/bin/ 
        export PATH=${IRACE_HOME}:$PATH
    ```
* Criar pasta para realizar a configuração do cenário
* Copiar template da pasta /path/to/R/irace/templates/*
* Tirar `.tmpl` de todos os arquivos

* Instalar pypy3
    ```
        $sudo apt install pypy3
    ```

* Instalar virtual env
    ```
        $cd src
        $virtualenv -p /usr/bin/pypy3 env_exp_irace
        $source env_exp_irace/bin/activate
        $pip install numpy
    ```

* Transformar `sa_backpack.py` em executável
    ```
        $chmod +x sa_backpack.py
    ```
* Testando configuração do `irace`:
    ```
        $irace --check
    ```
* Rodando o `irace`:
    ```
        $irace
    ```


## Arquivos auxiliares:

* __separate_instances.py__ -> script para separar as instâncias que inicialmente estavam em um único arquivo em diferentes arquivos
* __choose_train_instances.py__ -> script para escolher as instâncias de treino (escolhe 5% das instâncias de cada pasta)
* __testing.py__ -> script para rodar testes em paralelo

## Referências
* https://mlopez-ibanez.github.io/irace/
* https://cran.r-project.org/web/packages/irace/vignettes/irace-package.pdf

