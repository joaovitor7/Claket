from Dominio import *
from DATABASE import *



class RoteiroDAO():


    def inserir(Roteiro,Usuario):
        r = TabelaRoteiro(id=None, titulo=Roteiro.titulo, aceitacao=Roteiro.aceitacao, id_usuario=Usuario.cpf, data_avaliacao=Roteiro.data_da_avaliacao)
        db.session.add(r)
        db.session.flush()
        resultado_palavrachave=Roteiro.palavras_Chaves
        resultado_genero=Roteiro.generos
        for palavra in resultado_palavrachave:
            palavra_no_banco = TabelaPalavra_Chave.query.filter_by(palavra=palavra).first()
            if (palavra_no_banco == None):
                p = TabelaPalavra_Chave(id=None, palavra=palavra)
                db.session.add(p)
                db.session.flush()
                rp = TabelaRoteiro_Palavrachave(r.id, p.id)
                db.session.add(rp)
            else:
                rp = TabelaRoteiro_Palavrachave(r.id, palavra_no_banco.id)
                db.session.add(rp)
        for genero in resultado_genero:
            genero_no_banco = TabelaGenero.query.filter_by(genero=genero).first()
            if genero_no_banco is None:
                g = TabelaGenero(id=None, genero=genero)
                db.session.add(g)
                db.session.flush()
                rg = TabelaRoteiro_Genero(r.id, g.id)
                db.session.add(rg)
            else:
                rg = TabelaRoteiro_Genero(r.id, genero_no_banco.id)
                db.session.add(rg)
        db.session.commit()

        return True

    def listar(cpf):
        lista_de_roteiros = TabelaRoteiro.query.filter_by(id_usuario=cpf).all()
        return lista_de_roteiros

    def excluir(id):
        roteiro = TabelaRoteiro.query.filter_by(id=id).first()
        db.session.delete(roteiro)
        db.session.commit()

    def getRoteiro(id):
        roteiro = TabelaRoteiro.query.filter_by(id=id).first()
        palavras_chave = []
        generos = []
        id_palavras = TabelaRoteiro_Palavrachave.query.filter_by(id_roteiro=id).all()
        for x in id_palavras:
            palavra_chave = TabelaPalavra_Chave.query.filter_by(id=x.id_palavra_chave).first()
            palavras_chave.append(palavra_chave.palavra)
        id_generos= TabelaRoteiro_Genero.query.filter_by(id_roteiro=id).all()
        for y in id_generos:
            genero = TabelaGenero.query.filter_by(id=y.id_genero).first()
            generos.append(genero.genero)

        roteiroPesquisado=Roteiro(roteiro.titulo,palavras_chave,generos,roteiro.aceitacao,roteiro.data_avaliacao)

        return roteiroPesquisado


    def editar(id,Roteiro):
        roteiro = TabelaRoteiro.query.filter_by(id=id).first()
        roteiro.titulo=Roteiro.titulo

        palavrasChave = Roteiro.palavras_Chaves
        resultadoGenero = Roteiro.generos

        palavrasRelacionadas = TabelaRoteiro_Palavrachave.query.filter_by(id_roteiro=roteiro.id).all()
        generoRelacionados = TabelaRoteiro_Genero.query.filter_by(id_roteiro=roteiro.id).all()
        """palavrasLista=[]
        for palavraTemp in palavrasRelacionadas:
            id=palavraTemp.id
            palavraBusca = TabelaPalavra_Chave.query.filter_by(id=id).first()
            palavrasLista.append(palavraBusca)"""

        for palavraTemp in palavrasRelacionadas:
            db.session.delete(palavraTemp)
        for generoTemp in generoRelacionados:
            db.session.delete(generoTemp)

        for palavraChave in palavrasChave:
            palavra_no_banco = TabelaPalavra_Chave.query.filter_by(palavra=palavraChave).first()
            if (palavra_no_banco == None):
                p = TabelaPalavra_Chave(id=None, palavra=palavraChave)
                db.session.add(p)
                db.session.flush()
                rp = TabelaRoteiro_Palavrachave(roteiro.id, p.id)
                db.session.add(rp)
            else:
                rp = TabelaRoteiro_Palavrachave(roteiro.id, palavra_no_banco.id)
                db.session.add(rp)

        for genero in resultadoGenero:
            genero_no_banco = TabelaGenero.query.filter_by(genero=genero).first()
            rg = TabelaRoteiro_Genero(roteiro.id, genero_no_banco.id)
            db.session.add(rg)

        db.session.commit()





class GeneroDAO():

    @staticmethod
    def getGeneros():
        totalGeneros = TabelaGenero.query.all()
        return totalGeneros