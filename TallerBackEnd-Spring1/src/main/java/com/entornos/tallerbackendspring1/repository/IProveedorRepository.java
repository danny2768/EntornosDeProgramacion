package com.entornos.tallerbackendspring1.repository;

import com.entornos.tallerbackendspring1.model.Proveedor;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface IProveedorRepository extends JpaRepository<Proveedor,Integer> {
}
