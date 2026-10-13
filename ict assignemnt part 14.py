def loaded_dividers(vs, r1, r2, rl):
    v_unloaded = vs * (r2 / (r1 + r2))
    r_parallel = (r2 * rl) /(r2 + rl)
    v_loaded = vs * (r_parallel / (r1 + r_parallel))
    return (v_unloaded, v_loaded)
output = loaded_dividers(15, 2000, 2000, 1000)
print("loaded_divider(15, 2000, 2000, 1000) ->", output)
