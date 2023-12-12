import hyperopt


def ofn_custom_pyll():
    return {
        "abbr": "ofn-custom",
        "params": {
            "param_1": hyperopt.hp.uniformint("param_1", 0, 25),
            "param_2": hyperopt.hp.choice("param_2", [True, False]),
        },
    }
