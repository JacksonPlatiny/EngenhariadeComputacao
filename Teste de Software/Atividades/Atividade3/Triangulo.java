package Atividade3;

import java.lang.Math;

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

    public double calculaPerimetro() {
        return ladoA + ladoB + ladoC;
    }

    public double calculaArea() {
        if (!verificarExistenciaTriangulo()) {
            return 0.0; // Se não for um triângulo, a área é 0.
        }

        // fórmula de Heron.
        double s = calculaPerimetro() / 2;
        double area = Math.sqrt(s * (s - ladoA) * (s - ladoB) * (s - ladoC));
        return area;
    }

    private boolean verificarExistenciaTriangulo() {
        return (ladoA + ladoB > ladoC) && (ladoA + ladoC > ladoB) && (ladoB + ladoC > ladoA);
    }
}
