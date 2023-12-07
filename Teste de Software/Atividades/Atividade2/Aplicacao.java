package Atividade2;

public class Aplicacao {
    private Calculadora calculadora;

    public Aplicacao(String operacao) {
        this.calculadora = new Calculadora();
        calculadora.setOperacao(operacao);
    }

    public double realizaCalculo(double n1, double n2) {
        return calculadora.calcular(n1, n2);
    }
}
