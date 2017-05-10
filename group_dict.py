def group_dict(self, group_by='', dict_list=[], filter_keys=[]):
        """
        Group the data from a dict.

        This method receives a string representing the Dict Key it's going to
        be used to group the data, the list of Dicts you want to work on and
        the list of Keys you want to keep after grouping everything.
        The param 'filter_keys' is optional, if you don't inform any key,
        it's going to keep the original Dict.
        """
        if not isinstance(group_by, str) or len(group_by) == 0:
            return 0

        if not isinstance(dict_list, list) or len(dict_list) == 0:
            return 0
        else:
            for i in dict_list:
                if not isinstance(i, dict) or len(i.keys()) == 0:
                    return 0

        if not isinstance(filter_keys, list):
            return 0
        else:
            for idx, i in enumerate(filter_keys):
                if not isinstance(i, str) or len(i) == 0:
                    del filter_keys[idx]

        return {
            str(i): map(
                lambda y: len(filter_keys) > 0 and {
                    key: y[key] for key in filter_keys if key in y.keys()
                } or y, filter(lambda x: x[group_by] == i, dict_list)
            ) for i in list(
                set(
                    map(
                        lambda x: x[group_by], dict_list
                    )
                )
            )
        }
