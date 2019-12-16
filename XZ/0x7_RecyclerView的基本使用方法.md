## RecyclerView的基本使用方法

- 步骤

  1. 添加RecyclerView到布局中

  2. 根据RecyclerView的子项内容，创建子项布局以及对应需要的类和适配器

  3. 在活动中实现RecyclerView实例化并适配内容

     

- 本例只创建一个活动MainActivity

## 添加RecyclerView到布局中

- 要引用RecyclerView需要先在项目的build.gradle中（**app/build.gradle**）添加相应的依赖库，在dependencies闭包中添加两条依赖，并点击Sync Now同步

  ```java
  dependencies {
          
      implementation 'androidx.recyclerview:recyclerview:1.1.0'
      implementation 'androidx.recyclerview:recyclerview-selection:1.1.0-beta01'
  }
  ```

- 在MainActivity的布局activity_main.xml中添加RecyclerView

  ```java
  <LinearLayout android:layout_height="match_parent"
      android:layout_width="match_parent"
      xmlns:android="http://schemas.android.com/apk/res/android">
  
      <androidx.recyclerview.widget.RecyclerView
          android:id="@+id/recycler_view"
          android:layout_width="match_parent"
          android:layout_height="match_parent"/>
          
  </LinearLayout>
  ```



## 根据RecyclerView的子项内容，创建子项布局以及对应需要的类和适配器

- 本例用宝可梦作例子，子项内容为**宝可梦图片**和**宝可梦名字**

- 创建子项

  ```java
  <LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
      android:orientation="vertical"
      android:layout_width="match_parent"
      android:layout_height="wrap_content"
      android:layout_margin="10dp">
  
      <ImageView
          android:id="@+id/pokemon_image"
          android:layout_width="match_parent"
          android:layout_height="100dp"
          android:layout_gravity="center"/>
  
      <TextView
          android:id="@+id/pokemon_name"
          android:layout_width="wrap_content"
          android:layout_height="wrap_content"
          android:textSize="10dp"
          android:layout_gravity="left"/>
  
  </LinearLayout>
  ```

  - 根据个人需要对父布局、ImageView、TextView属性设置

- 创建Pokemon类

  ```java
  public class Pokemon {
      private String name;
      private int imageId;
  
      public Pokemon(String name, int imageId) {
          this.name = name;
          this.imageId = imageId;
      }
  
      public String getName() {
          return name;
      }
  
      public int getImageId() {
          return imageId;
      }
  
  }
  ```

  - Pokemon包含name和imageId（图片的路径）两个属性，和他们的两个get方法
  - 构造函数接收name 和 imageId两个参数

- 创建PokemonAdapter

  1. 定义数据队列 List<Pokemon> 以接收宝可梦们的数据，并用来加载到子项中
  2. 定义一个内部类ViewHolder，ViewHolder要继承自RecyclerView.ViewHolder，然后ViewHolder的内部构造函数要传入一个View参数，这个参数通常是子项的最外层布局，那我们就可以通过findViewById()方法来获取到布局中的ImageView和TextView实例了。
  3. 定义PokemonAdapter的构造函数。
  4. 因为PokemonAdapter继承自RecyclerView.Adapter，所以要重构onCreateViewHolder()、onBindViewHolder()、getItemCount()三个方法。

  ```java
  public class PokemonAdapter extends RecyclerView.Adapter<PokemonAdapter.ViewHolder> {
  
      private List<Pokemon> pokemonList;
  
      static class ViewHolder extends RecyclerView.ViewHolder{
          private ImageView pokemonImage;
          private TextView pokemonName;
          private View pokemonView;
  
          public ViewHolder(View view){
              super(view);
              pokemonImage = view.findViewById(R.id.pokemon_image);
              pokemonName = view.findViewById(R.id.pokemon_name);
              pokemonView = view;
          }
      }
  
      public PokemonAdapter(List<Pokemon> list){
          pokemonList = list;
      }
  
      @Override
      public ViewHolder onCreateViewHolder(@NonNull final ViewGroup parent, int viewType) {
          View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.pokemon_item,parent,false);
          final ViewHolder holder = new ViewHolder(view);
          holder.pokemonView.setOnClickListener(new View.OnClickListener() {
              @Override
              public void onClick(View v) {
                  int position = holder.getAdapterPosition();
                  Pokemon pokemon = pokemonList.get(position);
                  Toast.makeText(v.getContext(),"you click view" + pokemon.getName(),Toast.LENGTH_LONG).show();
              }
          });
          holder.pokemonImage.setOnClickListener(new View.OnClickListener() {
              @Override
              public void onClick(View v) {
                  int position = holder.getAdapterPosition();
                  Pokemon pokemon = pokemonList.get(position);
                  Toast.makeText(v.getContext(),"you clicked image" + pokemon.getName(),Toast.LENGTH_LONG).show();
              }
          });
  
          return holder;
      }
  
      @Override
      public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
          Pokemon pokemon = pokemonList.get(position);
          holder.pokemonImage.setImageResource(pokemon.getImageId());
          holder.pokemonName.setText(pokemon.getName());
      }
  
      @Override
      public int getItemCount() {
          return pokemonList.size();
      }
  ```

  - 我们在ViewHolder里又多定义了一个pokemonView来保存子项最外层布局的实例，这个实例和ImageView都被设置了点击事件。如果不需要点击事件，就把关于pokemonView相关的内容删除并且把fianl限定符去除即可。



## 在活动中实现RecyclerView实例化并适配内容

- MainActivity.java代码

  ```java
  public class MainActivity extends AppCompatActivity {
  
      private List<Pokemon> pokemonList = new ArrayList<>();
      @Override
      protected void onCreate(Bundle savedInstanceState) {
          super.onCreate(savedInstanceState);
          setContentView(R.layout.activity_main);
          initPokemon();
          RecyclerView recyclerView = findViewById(R.id.recycler_view);
          StaggeredGridLayoutManager layoutManager =  new StaggeredGridLayoutManager(3,StaggeredGridLayoutManager.VERTICAL);
          recyclerView.setLayoutManager(layoutManager);
          PokemonAdapter adapter = new PokemonAdapter(pokemonList);
          recyclerView.setAdapter(adapter);
  
  
      }
  
      private void initPokemon(){
          for(int i=0 ; i<10 ; i++){
              Pokemon pokemon = new Pokemon(getRandomLengthName("Pokemon : PiKaQiu"),R.drawable.pk);
              pokemonList.add(pokemon);
          }
      }
  
      private String getRandomLengthName(String name){
          Random random = new Random();
          int length = random.nextInt(20) + 1;
          StringBuilder builder = new StringBuilder();
          for(int i = 0 ; i < length ; i ++){
              builder.append(name);
          }
          return builder.toString();
      }
  }
  ```

- 先看initPokemon()和getRandomLengthName()方法，前者用于初始化宝可梦队列，这里我们只添加了皮卡丘的信息，10条！后者是用来改变宝可梦名字的长度的，这个操作是为了让瀑布流效果显示出来。（瀑布流好像在很多手机的便签里都有体现，就是分为左右两列的那种
- 在初始化Pokemon数据后，实例化RecyclerView，然后实例化一个布局管理器传入RecyclerView以达到设置RecyclerView布局的效果。本例使用StaggeredGridLayoutManager，和它一样的还有GridLayoutManager、LinearLayoutManager，它们创建一个布局管理器，然后用setLayoutManager将布局管理器传入RecyclerView内实现布局设置。布局管理器还可以详细定制，比如本例中，设置GridLayoutManager为三列，并且垂直分布（不懂看效果图就明白设置为三列什么意思了）。



## 效果图

![](https://ftp.bmp.ovh/imgs/2019/12/cbab56212ab208d8.png)