def agrupar_dict(self, agrupar_por='', lista_dict=[], filtro=[]):
        """
        Agrupar dados de um dicionario.

        Essa funcao recebe um string com a chave que sera usada como
        parametro para agrupar os dados, uma lista de dicionarios que seram
        agrupados e uma lista de chaves que serao mantidas nos dicionarios
        finais. Caso nao seja passado nenhum item em filtro, ele mantem o
        dicionario original.
        """
        if not isinstance(agrupar_por, str) or len(agrupar_por) == 0:
            return 0

        if not isinstance(lista_dict, list) or len(lista_dict) == 0:
            return 0
        else:
            for i in lista_dict:
                if not isinstance(i, dict) or len(i.keys()) == 0:
                    return 0

        if not isinstance(filtro, list):
            return 0
        else:
            for idx, i in enumerate(filtro):
                if not isinstance(i, str) or len(i) == 0:
                    del filtro[idx]

        return {
            str(i): map(
                lambda y: len(filtro) > 0 and {
                    key: y[key] for key in filtro if key in y.keys()
                } or y, filter(lambda x: x[agrupar_por] == i, lista_dict)
            ) for i in list(
                set(
                    map(
                        lambda x: x[agrupar_por], lista_dict
                    )
                )
            )
        }
