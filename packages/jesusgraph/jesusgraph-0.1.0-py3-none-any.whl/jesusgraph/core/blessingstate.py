from typing import Any, Dict, Optional, Iterator, Tuple, List

class BlessingState:
    """
    Gerencia o estado de bênçãos dentro do JesusGraph.

    Esta classe armazena e gerencia os valores recebidos durante a execução
    do grafo. Cada bênção tem um nome único e pode conter qualquer tipo de dado.
    
    O usuário pode interagir com as bênçãos de várias formas:
    - Usando os métodos específicos (addBlessing, getBlessing)
    - Usando a notação de dicionário (state["nome"])
    - Iterando sobre os itens (for name, value in state.items())
    """

    def __init__(self, initial_state: Optional[Dict[str, Any]] = None):
        """
        Inicializa o estado com um dicionário opcional de bênçãos.
        
        Args:
            initial_state: Dicionário inicial de bênçãos (opcional)
        """
        self._blessings: Dict[str, Any] = {}
        
        # Se um estado inicial foi fornecido, adicione-o
        if initial_state:
            for key, value in initial_state.items():
                self.addBlessing(key, value)

    def addBlessing(self, name: str, value: Any) -> 'BlessingState':
        """
        Adiciona uma nova bênção ao estado.

        Args:
            name (str): Nome da bênção (ex: 'resposta_ia')
            value (Any): Valor da bênção (pode ser qualquer tipo: string, dict, lista, etc)

        Returns:
            BlessingState: o próprio objeto para encadeamento de métodos
        """
        self._blessings[name] = value
        return self

    def getBlessing(self, name: str) -> Any:
        """
        Retorna uma bênção específica pelo nome.

        Args:
            name (str): Nome da bênção desejada

        Returns:
            Any: Valor armazenado ou None se não existir
        """
        return self._blessings.get(name, None)
    
    def updateBlessing(self, name: str, value: Any) -> 'BlessingState':
        """ 
        Atualiza o valor de uma bênção existente.

        Args:
            name (str): Nome da bênção a ser atualizada
            value (Any): Novo valor a ser atribuído
        
        Returns:
            BlessingState: o próprio objeto para encadeamento de métodos
            
        Raises:
            ValueError: Se a bênção não existir
        """
        if name not in self._blessings:
            raise ValueError(f"A blessing '{name}' ainda não existe. Use .addBlessing() para criar.")
        self._blessings[name] = value
        return self

    def hasBlessing(self, name: str) -> bool:
        """
        Verifica se uma bênção existe no estado.
        
        Args:
            name (str): Nome da bênção a verificar
        
        Returns:
            bool: True se a bênção existir, False caso contrário
        """
        return name in self._blessings

    def allBlessings(self) -> Dict[str, Any]:
        """
        Retorna todas as bênçãos armazenadas.

        Returns:
            Dict[str, Any]: Dicionário com todas as bênçãos
        """
        return self._blessings.copy()
        
    def items(self) -> Iterator[Tuple[str, Any]]:
        """
        Permite iterar sobre as bênçãos como em um dicionário.
        
        Returns:
            Um iterador sobre os pares (nome, valor) das bênçãos
        """
        return self._blessings.items()
        
    def keys(self) -> Iterator[str]:
        """
        Retorna os nomes de todas as bênçãos.
        
        Returns:
            Um iterador sobre os nomes das bênçãos
        """
        return self._blessings.keys()
        
    def values(self) -> Iterator[Any]:
        """
        Retorna os valores de todas as bênçãos.
        
        Returns:
            Um iterador sobre os valores das bênçãos
        """
        return self._blessings.values()

    def __getitem__(self, key: str) -> Any:
        """
        Permite acessar as bênçãos com colchetes, como em um dicionário:
            state["usuario"]

        Args:
            key (str): Nome da bênção

        Returns:
            Any: Valor da bênção ou None
        """
        return self._blessings.get(key, None)

    def __setitem__(self, key: str, value: Any) -> None:
        """
        Permite definir bênçãos com colchetes:
            state["resultado"] = {...}

        Args:
            key (str): Nome da bênção
            value (Any): Valor a ser armazenado
        """
        self._blessings[key] = value

    def __contains__(self, key: str) -> bool:
        """
        Permite verificar se uma bênção existe:
            if "usuario" in state:

        Args:
            key (str): Nome da bênção

        Returns:
            bool: True se existe, False se não
        """
        return key in self._blessings

    def __str__(self) -> str:
        """
        Representação amigável do estado com todas as bênçãos.
        """
        return f"Blessings: {self._blessings}"
        
    def __len__(self) -> int:
        """
        Retorna o número de bênçãos armazenadas.
        """
        return len(self._blessings)

    def __iter__(self) -> Iterator[str]:
        """
        Permite iterar diretamente sobre as chaves do estado.
        """
        return iter(self._blessings)

    def get(self, key: str, default: Any = None) -> Any:
        """
        Equivalente a getBlessing, mas com interface de dicionário.
        
        Args:
            key: Nome da blessing
            default: Valor padrão se não existir
            
        Returns:
            Valor da blessing ou valor padrão
        """
        return self._blessings.get(key, default)
