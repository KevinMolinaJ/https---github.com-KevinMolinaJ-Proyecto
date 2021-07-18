class usuario {
    rut;
    nombrecompleto;
    email;
    fechanac;
    //mutadores
    setRut(rut){
        this.rut=rut;
    }
    setNombrecompleto(nombrecompleto){
        this.nombrecompleto=nombrecompleto;
    }
    setEmail(email){
        this.email=email;
    }
    setFechanac(fechanac){
        this.fechanac=fechanac;
    }
    //accesador
    getRut(){
        return this.rut;
    }
    getNombrecompleto(){
        return this.nombrecompleto;
    }
    getEmail(){
        return this.email;
    }
    getFechanac(){
        return this.fechanac;
    }
}