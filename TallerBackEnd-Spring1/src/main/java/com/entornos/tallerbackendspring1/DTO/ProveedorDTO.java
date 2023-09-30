package com.entornos.tallerbackendspring1.DTO;

import com.fasterxml.jackson.annotation.JsonProperty;
import jakarta.persistence.Basic;
import lombok.Getter;
import lombok.Setter;

import java.io.Serial;
import java.io.Serializable;

@Getter
@Setter
public class ProveedorDTO implements Serializable {
    @Serial
    private static final long serialVersionUID = -8614315185327514631L;

    @JsonProperty("id")
    private Long id;

    @JsonProperty("ciudad")
    private String ciudad;

    @JsonProperty("direccion")
    private String direccion;

    @JsonProperty("nombre")
    private String nombre;

    @JsonProperty("telefono")
    private String telefono;

    @JsonProperty("nit")
    private String nit;
}
