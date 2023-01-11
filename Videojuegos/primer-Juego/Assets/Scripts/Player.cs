using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Player : MonoBehaviour
{
    public float Fuerza;
    private bool CambioDir;
    private Vector3 Dir;
    private Rigidbody RB;
    private AudioSource AudioMaster;
    public AudioClip AudioCoin;
    public GameObject Ccoins;
    public Text TextInt, TextFin;
    public Button BotonR;
    // Start is called before the first frame update
    void Start()
    {
       CambioDir = false;
        RB = this.gameObject.GetComponent<Rigidbody>();
            Dir = new Vector3(0, 0, 0);
        AudioMaster=this.gameObject.GetComponent<AudioSource>();
        TextInt.text = "No toque las monedas";
        TextFin.gameObject.SetActive(false);
    }
    private void FixedUpdate ()
    {
        RB.MovePosition(this.transform.position + Dir * Fuerza * Time.deltaTime);

    }
    // Update is called once per frame
    void Update()
    {
     if (Input.GetMouseButtonDown(0))
     {
         RB.Sleep();
        if(CambioDir == true)
        {
            Dir = new Vector3 (0,0,-1);
            CambioDir = false;
        }
        else
        {
            Dir = new Vector3 (-1,0,0);
            CambioDir = true;   
     }

    }
    if (this.transform.position.y < -2)
    {
        this.transform.position = new Vector3(5,1,4.5f);
        RB.Sleep ();
            Dir = new Vector3(0, 0, 0);
      }
        
    }
    private void OnTriggerEnter(Collider other)
    {
        if (other.tag == "Coin")
        {
            restartGame();
        }
        if(other.tag== "Meta")
        {
            TextInt.gameObject.SetActive(false);
            TextFin.gameObject.SetActive(true);
            //TextInt.text="Ganaste";
            //TextInt.color = new Color (93, 185, 50);
           // TextInt.transform.position= new Vector3 (82.85f, -63, 0);
            Fuerza = 0;
            RB.Sleep();

        }
    }
    public void restartGame()
    {
        this.transform.position = new Vector3(5,1,4.5f);
        RB.Sleep ();
            Dir = new Vector3(0,0,0);
            for (int i=0; i<Ccoins.transform.childCount; i++)
            {
                Ccoins.transform.GetChild(i).gameObject.SetActive(true);
            }
    }
    }
