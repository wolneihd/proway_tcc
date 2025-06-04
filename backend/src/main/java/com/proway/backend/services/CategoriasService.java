package com.proway.backend.services;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.proway.backend.models.Categoria;
import com.proway.backend.repositories.CategoriaRepository;

@Service
public class CategoriasService {
    
    @Autowired
    private CategoriaRepository categoriaRepository;

    public List<Categoria> findAll() {
        return categoriaRepository.findAll();     
    }

}
