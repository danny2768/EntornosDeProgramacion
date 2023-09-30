package com.entornos.tallerbackendspring1.model;


import jakarta.persistence.*;
import lombok.Data;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.io.Serial;
import java.io.Serializable;

@Entity
@Data
@NoArgsConstructor
@Table(schema = "taller1", name = "Proveedor")
public class Proveedor implements Serializable {
    @Serial
    private static final long serialVersionUID = -5480542936504183626L;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id", nullable = false)
    private Long id;

    @Column(name = "ciudad", nullable = false, length = 255)
    private String ciudad;

    @Column(name = "direccion", nullable = false, length = 255)
    private String direccion;

    @Column(name = "nombre", nullable = false, length = 255)
    private String nombre;

    @Column(name = "telefono", nullable = false, length = 15)
    private String telefono;

    @Column(name = "nit", nullable = false, length = 100)
    private String nit;
}
