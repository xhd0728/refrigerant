def cal_refrigeration_params(h_0, h_1, h_2, h_3, h_4, v_1, n_i, r, Q) -> dict:
    param_list = []
    for arg in cal_refrigeration_params.__code__.co_varnames:
        if arg != "self" and arg != "cls" and arg not in locals() and arg not in globals():
            param_list.append(arg)
    try:
        q_0 = h_0 - h_4
        q_zv = q_0 / v_1
        w = h_2 - h_1
        w_i = w / n_i
        h_2s = w_i - h_1
        COP = q_0 / w
        COP_i = q_0 / w_i
        q_k = h_2s - h_3
        q_m = Q / q_0
        q_vs = q_m * v_1
        q_vh = q_vs / r
        P = q_m * w
        P_i = P / n_i
        Q_k = q_m * q_k
        n = COP / COP_i
    except Exception as e:
        return {"error": str(e), "param_required": param_list}
    else:
        return {
            "q_0": q_0,
            "q_zv": q_zv,
            "w": w,
            "w_i": w_i,
            "h_2s": h_2s,
            "COP": COP,
            "COP_i": COP_i,
            "q_k": q_k,
            "q_m": q_m,
            "q_vs": q_vs,
            "q_vh": q_vh,
            "P": P,
            "P_i": P_i,
            "Q_k": Q_k,
            "n": n
        }
