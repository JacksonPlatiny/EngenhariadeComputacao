package Atividade2;

public class Calculadora {
    private String operacao;

    public void setOperacao(String operacao) {
        this.operacao = operacao;
    }

    public String getOperacao() {
        return operacao;
    }

    public double calcular(double n1, double n2) {
        switch (operacao) {
            case "soma":
                return n1 + n2;
            case "subtracao":
                return n1 - n2;
            case "multiplicacao":
                return n1 * n2;
            case "divisao":
                if (n2 == 0) {
                    throw new ArithmeticException("Divisão por zero não é permitida.");
                }
                return n1 / n2;
            default:
                throw new IllegalArgumentException("Operação não suportada: " + operacao);
        }
    }
}
