import static org.junit.Assert.*;
import java.util.ArrayList;
import org.junit.Before;
import org.junit.Test;

public class ServicoTest {
    private Mecanico mecanico;
    private Veiculo veiculo;
    private Servico servico;

    @Before
    public void setUp() {
        mecanico = new Mecanico("123", "João", new ArrayList<>());
        veiculo = new Veiculo("ABC123", "CARRO POPULAR", 0, 2022);
        servico = new Servico(1, mecanico, veiculo);
    }

    @Test
    public void testGettersESetters() {
        assertEquals(1, servico.getID());
        assertNull(servico.getMotivo());
        assertSame(mecanico, servico.getMecanico());
        assertSame(veiculo, servico.getVeiculo());

        servico.setID(2);
        servico.setMotivo("Problema no motor");

        assertEquals(2, servico.getID());
        assertEquals("Problema no motor", servico.getMotivo());
    }

    @Test
    public void testOrdemServico() {
        assertNull(servico.getMotivo());
        assertEquals(0, veiculo.getNumOcorrencias());

        servico.ordemServico("Problema no motor");

        assertEquals("Problema no motor", servico.getMotivo());
        assertEquals(1, veiculo.getNumOcorrencias());
    }
}
