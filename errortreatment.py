def tratamento(checkresponse): #Função para tratamento de erros
    import logging

    #Diretório de log
    dirLog = "C:\\Bancamais\\Fastcommerce\\Logs\\LogProdUni\\log_file.log"

    #Configuração do logger
    logger = logging.getLogger('my_logger') #Cria o objeto de log
    logger.setLevel(logging.INFO) #Configura o nível de log
    handler = logging.FileHandler(f'{dirLog}') #Cria arquivo handler
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S') #Define o formato do log
    handler.setFormatter(formatter) #Define o formato do log para o handler
    logger.addHandler(handler) #Adiciona o handler ao logger

    #Funções para tratamento de erros
    global errodesc
    errodesc = []
    index1 = checkresponse.find("<ErrCod>1</ErrCod>")
    index2 = checkresponse.find("<ErrCod>2</ErrCod>")
    index3 = checkresponse.find("<ErrCod>3</ErrCod>")
    index4 = checkresponse.find("<ErrCod>4</ErrCod>")
    index5 = checkresponse.find("<ErrCod>5</ErrCod>")
    index6 = checkresponse.find("<ErrCod>6</ErrCod>")
    index7 = checkresponse.find("<ErrCod>7</ErrCod>")
    index8 = checkresponse.find("<ErrCod>8</ErrCod>")
    index9 = checkresponse.find("<ErrCod>9</ErrCod>")
    index10 = checkresponse.find("<ErrCod>10</ErrCod>")
    index11 = checkresponse.find("<ErrCod>11</ErrCod>")
    index12 = checkresponse.find("<ErrCod>12</ErrCod>")
    index13 = checkresponse.find("<ErrCod>13</ErrCod>")
    index14 = checkresponse.find("<ErrCod>14</ErrCod>")
    index15 = checkresponse.find("<ErrCod>15</ErrCod>")
    index16 = checkresponse.find("<ErrCod>16</ErrCod>")
    index17 = checkresponse.find("<ErrCod>17</ErrCod>")
    index18 = checkresponse.find("<ErrCod>18</ErrCod>")
    if index1 > 1:
        errodesc = "Loja não encontrada"
    elif index2 > 1:
        errodesc = "Usuario Inválido"
    elif index3 > 1:
        errodesc = "Sem Senha"
    elif index4 > 1:
        errodesc = "Erro de Login"
    elif index5 > 1:
        errodesc = "Endereço IP Bloqueado"
    elif index6 > 1:
        errodesc = "Muitas Tentativas. Usuario suspenso por 3 minutos"
    elif index7 > 1:
        errodesc = "Erro de Login. Proximo login invalido suspenderá o usuario por 3 minutos"
    elif index8 > 1:
        errodesc = "Método 19 inválido. Ordens inválidas nos registros XML"
    elif index9 > 1:
        errodesc = "Report/Utility não encontrado ou acesso negado. Limite de 20 acessos por hora atingido"
    elif index10 > 1:
        errodesc = "Accesso à API negado"
    elif index11 > 1:
        errodesc = "Erro de Report/Utility"
    elif index12 > 1:
        errodesc = "StoreID inválido para este login"
    elif index13 > 1:
        errodesc = "StoreID não informado"
    elif index14 > 1:
        errodesc = "Loja suspensa"
    elif index15 > 1:
        errodesc = "Periodo de demostração finalizado"
    elif index16 > 1:
        errodesc = "XMLRecords não informado"
    elif index17 > 1:
        errodesc = "Acesso negado"
    elif index18 > 1:
        errodesc = "Produto(s) inválido(s) no XMLRecords"
    
    if errodesc == []:
        logger.info("Produto incluido com sucesso!")
    else:
        with open("C:\\Bancamais\\Fastcommerce\\Erros\\ErrosXMLProdUni\\Erro.txt", "w+") as f:
            f.write(f"{errodesc}")
            f.write(f"\n{checkresponse}")
            f.close()
        logger.error(errodesc)
    
    #Fecha o logger
    logging.shutdown()
