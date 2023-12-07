package Atividade2;

public class Biblioteca {
    private String nome;
    private String CNPJ;
    private int anoFundacao;

    public Biblioteca(String nome, String CNPJ, int anoFundacao) {
        this.nome = nome;
        this.CNPJ = CNPJ;
        this.anoFundacao = anoFundacao;
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
}
