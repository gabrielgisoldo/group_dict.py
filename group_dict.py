def group_dict(self, group_by='', dict_list=[], filter_keys=[]):
        """
        Group the data from a dict.

        This method receives a value representing the Dict Key it's going to
        be used to group the data, the list of Dicts you want to work on and
        the list of Keys you want to keep after grouping everything.
        The param 'filter_keys' is optional, if you don't inform any key,
        it's going to keep the original Dict.
        """
        if not group_by:
            return "No key to group by informed."

        if not isinstance(dict_list, [list, tuple]) or len(dict_list) == 0:
            return "dict_list should be a valid list/tuple."
        else:
            for i in dict_list:
                if not isinstance(i, dict) or len(i.keys()) == 0:
                    return "Every item inside the list(dict_list) should be a valid Dict."

        if not isinstance(filter_keys, [list, tuple]):
            return 0

            return {
                i: map(
                    lambda y: len(filter_keys) > 0 and {
                        key: y[key] for key in filter_keys if key in y.keys()
                    } or y, filter(lambda x: x[group_by] == i, dict_list)
                ) for i in list(
                    set(
                        map(
                            lambda x: x[group_by],
                            filter(
                                lambda k: group_by in k.keys(), dict_list
                            )
                        )
                    )
                )
            }
