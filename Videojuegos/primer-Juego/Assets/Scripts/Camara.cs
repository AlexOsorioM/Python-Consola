using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class Camara : MonoBehaviour
{
    public GameObject Player;
    private Vector3 PosIni;
    // Start is called before the first frame update
    void Start()
    {
        PosIni = this.gameObject.transform.position - Player.gameObject.transform.position;
    }


    // Update is called once per frame
    void Update()
    {
        this.gameObject.transform.position = Player.gameObject.transform.position + PosIni;
    }
}