package Atividade1;

public class Triangulo {
    private double ladoA;
    private double ladoB;
    private double ladoC;

    public Triangulo(double ladoA, double ladoB, double ladoC) {
        this.ladoA = ladoA;
        this.ladoB = ladoB;
        this.ladoC = ladoC;
    }

    public String classificarTriangulo() {
        if (!verificarExistenciaTriangulo()) {
            return "Não é um triângulo";
        }

        if (ladoA == ladoB && ladoB == ladoC) {
            return "Equilátero";
        } else if (ladoA == ladoB || ladoB == ladoC || ladoA == ladoC) {
            return "Isósceles";
        } else {
            return "Escaleno";
        }
    }

    private boolean verificarExistenciaTriangulo() {
        return (ladoA + ladoB > ladoC) && (ladoA + ladoC > ladoB) && (ladoB + ladoC > ladoA);
    }
}
