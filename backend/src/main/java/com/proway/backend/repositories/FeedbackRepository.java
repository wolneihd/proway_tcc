package com.proway.backend.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import com.proway.backend.models.Feedback;

public interface FeedbackRepository extends JpaRepository<Feedback, Long> {
    
}  