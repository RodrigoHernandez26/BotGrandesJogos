def handler (ctx, error):
    try:
        vars(ctx.args[0].add)
        vars(ctx.args[0].jokenpo)
        vars(ctx.args[0].novo)
        vars(ctx.args[0].remover)
        vars(ctx.args[0].retirar)
        vars(ctx.args[0].setadm)
        vars(ctx.args[0].var)   
    except Exception as e:
        print(e)