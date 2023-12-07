package Atividade2;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class AplicacaoTest {

    @Test
    public void testSoma() {
        Aplicacao aplicacao = new Aplicacao("soma");
        double resultado = aplicacao.realizaCalculo(5, 3);
        assertEquals(8.0, resultado);
    }

    @Test
    public void testSubtracao() {
        Aplicacao aplicacao = new Aplicacao("subtracao");
        double resultado = aplicacao.realizaCalculo(5, 3);
        assertEquals(2.0, resultado);
    }

    @Test
    public void testMultiplicacao() {
        Aplicacao aplicacao = new Aplicacao("multiplicacao");
        double resultado = aplicacao.realizaCalculo(5, 3);
        assertEquals(15.0, resultado);
    }

    @Test
    public void testDivisao() {
        Aplicacao aplicacao = new Aplicacao("divisao");
        double resultado = aplicacao.realizaCalculo(6, 2);
        assertEquals(3.0, resultado);
    }

    @Test
    public void testDivisaoPorZero() {
        Aplicacao aplicacao = new Aplicacao("divisao");
        assertThrows(ArithmeticException.class, () -> aplicacao.realizaCalculo(5, 0));
    }

}
