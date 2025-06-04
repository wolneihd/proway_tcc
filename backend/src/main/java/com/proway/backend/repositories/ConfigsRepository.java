package com.proway.backend.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import com.proway.backend.models.Configs;

public interface ConfigsRepository extends JpaRepository<Configs, Long> {
    
}
