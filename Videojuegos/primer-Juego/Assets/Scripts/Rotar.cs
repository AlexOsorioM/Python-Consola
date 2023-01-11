using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Rotar: MonoBehaviour
{
    public float FrotarZ;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        this.gameObject.transform.Rotate(new Vector3(90,0,  FrotarZ) * Time.deltaTime);
        
    }
}
