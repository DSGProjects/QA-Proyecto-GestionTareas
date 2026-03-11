-- Ver todos los resultados
SELECT * FROM resultados;

-- Ver solo los PASSED
SELECT * FROM resultados WHERE status = 'PASSED';

-- Contar cuántos tests pasaron
SELECT COUNT(*) as total_passed FROM resultados WHERE status = 'PASSED';

-- Ver el último test ejecutado
SELECT * FROM resultados ORDER BY fecha DESC LIMIT 1;