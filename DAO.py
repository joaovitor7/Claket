from Dominio import *
from DATABASE import *
from datetime import *

class RoteiroDAO():


    def inserir(roteiro, usuario):
        tabelaRoteiro = TabelaRoteiro(id = None, titulo = roteiro.getTitulo(), aceitacao = roteiro.getAceitacao(), id_usuario = usuario.getCpf(), data_avaliacao = roteiro.getDataAvaliacao())
        db.session.add(tabelaRoteiro)
        db.session.flush()
        resultadoPalavraChave = roteiro.getPalavrasChave()
        resultadoGenero = roteiro.getGeneros()
        PalavraChaveDAO.inserir(resultadoPalavraChave, tabelaRoteiro)
        GeneroDAO.inserir(resultadoGenero, tabelaRoteiro)
        db.session.commit()

        return True

    def listar(cpf):
        roteirosUsuario = []
        tabelaRoteiroLista = TabelaRoteiro.query.filter_by(id_usuario = cpf).all()


        for roteiroTemp in tabelaRoteiroLista:

            palavrasChave = []
            generos = []

            palavrasRelacionadas = TabelaRoteiroPalavraChave.query.filter_by(id_roteiro=roteiroTemp.id).all()
            generoRelacionados = TabelaRoteiroGenero.query.filter_by(id_roteiro=roteiroTemp.id).all()

            for palavraTemp in palavrasRelacionadas:
                palavraChave = PalavraChaveDAO.getPalavraChave(palavraTemp.id_palavra_chave)

                palavrasChave.append(palavraChave)
            for generoTemp in generoRelacionados:
                genero = GeneroDAO.getGenero(generoTemp.id_genero)
                generos.append(genero)

            roteiro=Roteiro(roteiroTemp.id,roteiroTemp.titulo,palavrasChave,generos,roteiroTemp.aceitacao, str(roteiroTemp.data_avaliacao))
            roteirosUsuario.append(roteiro)

        return roteirosUsuario

    def excluir(id):
        tabelaRoteiro = TabelaRoteiro.query.filter_by(id = id).first()
        db.session.delete(tabelaRoteiro)
        db.session.commit()

    def getRoteiro(id):
        tabelaRoteiro = TabelaRoteiro.query.filter_by(id = id).first()
        palavras_chave = []
        generos = []
        tabelaRoteiroPalavraChaveLista = TabelaRoteiroPalavraChave.query.filter_by(id_roteiro = id).all()
        for palavraTemp in tabelaRoteiroPalavraChaveLista:
            palavraChave = PalavraChaveDAO.getPalavraChave(palavraTemp.id_palavra_chave)
            palavras_chave.append(palavraChave)
        tabelaRoteiroGeneroLista = TabelaRoteiroGenero.query.filter_by(id_roteiro = id).all()
        for generoTemp in tabelaRoteiroGeneroLista:
            genero = GeneroDAO.getGenero(generoTemp.id_genero)
            generos.append(genero)

        roteiroPesquisado = Roteiro(tabelaRoteiro.id,tabelaRoteiro.titulo, palavras_chave, generos ,tabelaRoteiro.aceitacao ,tabelaRoteiro.data_avaliacao)

        return roteiroPesquisado


    def editar(roteiro):
        tabelaRoteiro = TabelaRoteiro.query.filter_by(id = roteiro.getId()).first()
        tabelaRoteiro.titulo = roteiro.getTitulo()

        resultadoPalavrasChave = roteiro.getPalavrasChave()
        resultadoGenero = roteiro.getGeneros()

        palavrasRelacionadas = TabelaRoteiroPalavraChave.query.filter_by(id_roteiro = tabelaRoteiro.id).all()
        generoRelacionados = TabelaRoteiroGenero.query.filter_by(id_roteiro = tabelaRoteiro.id).all()

        for palavraTemp in palavrasRelacionadas:
            db.session.delete(palavraTemp)
        for generoTemp in generoRelacionados:
            db.session.delete(generoTemp)

        PalavraChaveDAO.inserir(resultadoPalavrasChave, tabelaRoteiro)
        GeneroDAO.inserir(resultadoGenero, tabelaRoteiro)

        db.session.commit()
    def setNota(id ,nota):
        tabelaRoteiro = TabelaRoteiro.query.filter_by(id=id).first()
        tabelaRoteiro.data_avaliacao = datetime.now().strftime('%Y-%m-%d')
        tabelaRoteiro.aceitacao = nota
        db.session.commit()

class GeneroDAO():

    @staticmethod
    def getGeneros():
        totalGeneros = []
        tabelaGenero = TabelaGenero.query.all()
        for generoTemp in tabelaGenero:
            totalGeneros.append(generoTemp.genero)

        return totalGeneros

    def inserir(generos, tabelaRoteiro):
        for generoTemp in generos:
            genero_no_banco = TabelaGenero.query.filter_by(genero = generoTemp).first()
            tabelaRoteiroGenero = TabelaRoteiroGenero(tabelaRoteiro.id, genero_no_banco.id)
            db.session.add(tabelaRoteiroGenero)
        db.session.commit()

    def getGenero(id):
        tabelaGenero = TabelaGenero.query.filter_by(id=id).first()
        genero = tabelaGenero.genero
        return genero


class PalavraChaveDAO():

    def inserir(palavrasChaves, tabelaRoteiro):

        for palavraTemp in palavrasChaves:
            palavraChave = palavraTemp.getTag()
            palavra_no_banco = TabelaPalavraChave.query.filter_by(palavra = palavraChave).first()
            if (palavra_no_banco == None):
                tabelaPalavraChave = TabelaPalavraChave(id = None, palavra = palavraChave)
                db.session.add(tabelaPalavraChave)
                db.session.flush()
                tabelaRoteiroPalavraChave = TabelaRoteiroPalavraChave(tabelaRoteiro.id, tabelaPalavraChave.id)

                tabelaSentimento = TabelaSentimento.query.filter_by(sentimento = palavraTemp.getSentimento()).first()

                tabelaSentimentoPalavraChave = TabelaSentimentoPalavraChave(tabelaSentimento.id, tabelaPalavraChave.id,'1990/12/12', 0)

                db.session.add(tabelaRoteiroPalavraChave)
                db.session.add(tabelaSentimentoPalavraChave)
                db.session.commit()
            else:
                relacao_no_banco = TabelaRoteiroPalavraChave.query.filter_by(id_roteiro = tabelaRoteiro.id,
                                                                             id_palavra_chave = palavra_no_banco.id).first()
                if (relacao_no_banco == None):

                    tabelaRoteiroPalavraChave = TabelaRoteiroPalavraChave(tabelaRoteiro.id, palavra_no_banco.id)
                    db.session.add(tabelaRoteiroPalavraChave)
                    db.session.commit()

    def getPalavraChave(id):
        tabelaPalavraChave = TabelaPalavraChave.query.filter_by(id=id).first()

        tabelaSentimentoPalavraChaveOrdenada = TabelaSentimentoPalavraChave.query.order_by(
            (TabelaSentimentoPalavraChave.data).desc()).all()

        for tabelaSentimentoPalavraChave in tabelaSentimentoPalavraChaveOrdenada:

            if tabelaSentimentoPalavraChave.id_palavra_chave == id:
                tabelaSentimento = TabelaSentimento.query.filter_by(
                    id=tabelaSentimentoPalavraChave.id_sentimento).first()

                palavraChave = PalavraChave(tabelaPalavraChave.id, tabelaPalavraChave.palavra,
                                            tabelaSentimento.sentimento, tabelaSentimentoPalavraChave.qnt_de_tweets)

                return palavraChave

    def atualizarSentimento(palavraChave):

        tabelaPalavraChave = TabelaPalavraChave.query.filter_by(palavra=palavraChave.getTag()).first()

        tabelaSentimento = TabelaSentimento.query.filter_by(sentimento=palavraChave.getSentimento()).first()

        data = datetime.now().strftime('%Y-%m-%d')

        tabelaSentimentoPalavraChave = TabelaSentimentoPalavraChave.query.filter_by(id_palavra_chave =tabelaPalavraChave.id, data = data).first()
        if (tabelaSentimentoPalavraChave == None):

            tabelaSentimentoPalavraChave = TabelaSentimentoPalavraChave(tabelaSentimento.id, tabelaPalavraChave.id, data,
                                                                        palavraChave.getQntTweets())

            db.session.add(tabelaSentimentoPalavraChave)
            db.session.commit()

class UsuarioDAO():
    def setPlano(idUsuario, idPlano):
        tabelaUsuario =  TabelaUsuario.query.filter_by(cpf = idUsuario).first()
        tabelaUsuario.id_plano = idPlano
        db.session.commit()