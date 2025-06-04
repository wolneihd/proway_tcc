package com.proway.backend.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import com.proway.backend.models.Categoria;

public interface CategoriaRepository extends JpaRepository<Categoria, Long> {
    
} 