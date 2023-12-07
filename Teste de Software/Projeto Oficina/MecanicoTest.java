import static org.junit.Assert.*;
import org.junit.Test;
import java.util.ArrayList;
import java.util.List;

public class MecanicoTest {

    @Test
    public void testFuncionarioPremiumComMaisDeDuasEspecialidades() {
        List<String> especialidades = new ArrayList<>();
        especialidades.add("Motor");
        especialidades.add("Transmissão");
        especialidades.add("Freios");
        
        Mecanico mecanico = new Mecanico("123", "João", especialidades);
        
        assertTrue(mecanico.funcionarioPremium());
    }

    @Test
    public void testFuncionarioPremiumComDuasEspecialidades() {
        List<String> especialidades = new ArrayList<>();
        especialidades.add("Motor");
        especialidades.add("Transmissão");
        
        Mecanico mecanico = new Mecanico("456", "Maria", especialidades);
        
        assertTrue(mecanico.funcionarioPremium());
    }

    @Test
    public void testGettersESetters() {
        Mecanico mecanico = new Mecanico("789", "Carlos", new ArrayList<>());
        
        mecanico.setMatricula("987");
        mecanico.setNome("Carlos Silva");
        mecanico.setEspecialidades(List.of("Suspensão", "Freios"));
        
        assertEquals("987", mecanico.getMatricula());
        assertEquals("Carlos Silva", mecanico.getNome());
        assertEquals(List.of("Suspensão", "Freios"), mecanico.getEspecialidades());
    }
}