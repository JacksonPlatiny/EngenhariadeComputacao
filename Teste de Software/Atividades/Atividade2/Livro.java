package Atividade2;

public class Livro {
    private String nome;
    private int edicao;
    private String autor;
    private String ISBN;

    public Livro(String nome, int edicao, String autor, String ISBN) {
        this.nome = nome;
        this.edicao = edicao;
        this.autor = autor;
        this.ISBN = ISBN;
    }
    
    public String getNome() {
        return nome;
    }
    
    public void setNome(String nome) {
        this.nome = nome;
    }
    
    public int getEdicao() {
        return edicao;
    }
    
    public void setEdicao(int edicao) {
        this.edicao = edicao;
    }
    
    public String getAutor() {
        return autor;
    }
    
    public void setAutor(String autor) {
        this.autor = autor;
    }
    
    public String getISBN() {
        return ISBN;
    }
    
    public void setISBN(String ISBN) {
        this.ISBN = ISBN;
    }
    
    public boolean verificaLancamento() {
        return edicao > 2022;
    }
    
}
