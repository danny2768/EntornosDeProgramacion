package com.entornos.tallerbackendspring1.DTO;

import org.antlr.v4.runtime.misc.NotNull;
import org.springframework.lang.NonNull;

import java.io.Serial;
import java.io.Serializable;

public class ProveedorDTO implements Serializable {
    @Serial
    private static final long serialVersionUID = -8614315185327514631L;

    private Long id;

    @NotNull
    private String ciudad;

    @NotNull
    private String direccion;

    @NotNull
    private String nombre;

    @NotNull
    private String telefono;

    @NotNull
    private String nit;
}
