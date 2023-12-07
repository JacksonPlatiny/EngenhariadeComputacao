package Atividade2;

import java.util.ArrayList;
import java.util.List;

public class Biblioteca2 {
    private String nome;
    private String CNPJ;
    private int anoFundacao;
    private List<Livro> listaLivros;

    public Biblioteca2(String nome, String CNPJ, int anoFundacao) {
        this.nome = nome;
        this.CNPJ = CNPJ;
        this.anoFundacao = anoFundacao;
        this.listaLivros = new ArrayList<>();
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getCNPJ() {
        return CNPJ;
    }

    public void setCNPJ(String CNPJ) {
        this.CNPJ = CNPJ;
    }

    public int getAnoFundacao() {
        return anoFundacao;
    }

    public void setAnoFundacao(int anoFundacao) {
        this.anoFundacao = anoFundacao;
    }

    public boolean patrimonioHistorico() {
        return anoFundacao < 1980;
    }

    public void incluirLivro(Livro livro) {
        listaLivros.add(livro);
    }

    public void removerLivro(Livro livro) {
        listaLivros.remove(livro);
    }

    public List<Livro> consultarLivros() {
        return listaLivros;
    }

    public boolean acervoPremium() {
        int countLancamentos = 0;
        for (Livro livro : listaLivros) {
            if (livro.verificaLancamento()) {
                countLancamentos++;
                if (countLancamentos >= 5) {
                    return true;
                }
            }
        }
        return false;
    }

    public void setListaLivros(List<Livro> listaLivros) {
        this.listaLivros = listaLivros;
    }

    public List<Livro> getListaLivros() {
        return listaLivros;
    }
}
