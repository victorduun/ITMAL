def reload():
    #Reload module:
    import importlib
    from data_help import data_loader
    importlib.reload(data_loader)


reload()