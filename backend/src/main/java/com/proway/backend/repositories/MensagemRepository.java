package com.proway.backend.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import com.proway.backend.models.Mensagem;

public interface MensagemRepository extends JpaRepository<Mensagem, Long> {
    
}
