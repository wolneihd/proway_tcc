package com.proway.backend.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import com.proway.backend.models.Usuario;

public interface UsuarioRepository extends JpaRepository<Usuario, Long> {
    
    boolean existsByIdTelegram(Long idTelegram);
    Usuario findByIdTelegram(long idTelegram);
}
