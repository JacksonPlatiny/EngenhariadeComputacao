import static org.junit.Assert.*;
import org.junit.Test;

public class VeiculoTest {

    @Test
    public void testCalculaGarantiaParaPickup() {
        Veiculo veiculo = new Veiculo("ABC123", "PICKUP", 0, 2023);
        assertEquals(2025, veiculo.calculaGarantia());
    }

    @Test
    public void testCalculaGarantiaParaSUV() {
        Veiculo veiculo = new Veiculo("XYZ789", "SUV", 1, 2024);
        assertEquals(2026, veiculo.calculaGarantia());
    }

    @Test
    public void testCalculaGarantiaParaCarroPopular() {
        Veiculo veiculo = new Veiculo("DEF456", "CARRO POPULAR", 2, 2025);
        assertEquals(2027, veiculo.calculaGarantia());
    }

    @Test
    public void testGettersESetters() {
        Veiculo veiculo = new Veiculo("GHI789", "SUV", 2, 2022);
        
        veiculo.setPlaca("JKL456");
        veiculo.setTipo("PICKUP");
        veiculo.setNumOcorrencias(3);
        veiculo.setAnoFabricacao(2021);
        
        assertEquals("JKL456", veiculo.getPlaca());
        assertEquals("PICKUP", veiculo.getTipo());
        assertEquals(3, veiculo.getNumOcorrencias());
        assertEquals(2021, veiculo.getAnoFabricacao());
    }
}